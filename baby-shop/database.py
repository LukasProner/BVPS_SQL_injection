import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "shop.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.executescript("""
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS customers;
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS users;

        CREATE TABLE products (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            price       REAL NOT NULL,
            description TEXT
        );

        CREATE TABLE users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role     TEXT DEFAULT 'user'
        );

        CREATE TABLE customers (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name      TEXT NOT NULL,
            email          TEXT NOT NULL,
            phone          TEXT,
            address        TEXT,
            credit_card    TEXT,
            date_of_birth  TEXT
        );

        CREATE TABLE orders (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            product_id  INTEGER NOT NULL,
            order_date  TEXT NOT NULL,
            quantity    INTEGER DEFAULT 1,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (product_id)  REFERENCES products(id)
        );

        INSERT INTO products (name, price, description) VALUES
            ('Kocik Maxi Cosi Zelia', 290.00, 'lahky kombi kocik 3v1'),
            ('Kocik Bugaboo Fox 5', 1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex', 450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux', 750.00, 'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring', 500.00, 'lahky mestsky kocik'),
            ('Kocik Hauck Rapid 4', 190.00, 'ekonomicky kocik nastavitelna opierka chrbta radsej do mesta'),
            ('Kočík Maxi-Cosi Zelia',   299.99,  'Ľahký kombikočík 3v1, vhodný od narodenia.'),
            ('Kočík Bugaboo Fox 5',     1199.00, 'Prémiový kočík s odpruženým podvozkom.'),
            ('Kočík Joie Mytrax Flex',   449.50, 'Skladací kočík s otočnou sedačkou.'),
            ('Kočík Chicco Trio Best Friend', 349.00, 'Trio systém kompatibilný s autosedačkou Chicco.'),
            ('Kočík Silver Cross Wave',  899.00, 'Tandemový kočík pre dvoch detí, elegantný dizajn.'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Chicco Trio Best Friend', 350.00, 'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kočík Cybex Balios S Lux', 749.90, 'Reverzibilná sedačka, vhodný od narodenia do 22 kg.'),
            ('Kočík Thule Spring',       499.00, 'Ľahký mestský kočík, skladný a manévrovateľný.'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti'),
            ('Kocik Silver Cross Wave', 890.00, 'tandem pre 2 deti');

        INSERT INTO users (username, password, role) VALUES
            ('admin', 'tajneheslo123', 'admin'),
            ('jan',   'heslo456',      'user'),
            ('palo',  'heslo456',      'user'),
            ('marek', 'heslo456',      'user'),
            ('hetes', 'heslo456',      'user'),
            ('juro',  'heslo456',      'user'),
            ('peto',  'heslo456',      'user'),
            ('milan', 'heslo456',      'user');

        INSERT INTO customers (full_name, email, phone, address, credit_card, date_of_birth) VALUES
            ('Jana Kovacova',    'jana.jana@email.sk',    '0911 123 456', 'Hlavna 12, Bratislava',        '4111 1111 1111 1111', '1990-03-15'),
            ('Peter Novak',      'peter.peter@gmail.com',     '0944 987 654', 'Namestie SNP 3, Banska Bystrica', '5500 0055 5555 5559', '1985-07-22'),
            ('Maria Horvathova', 'maria.ho@gmail.com',     '0902 555 777', 'Obchodna 8, Kosice',            '3714 496353 98431',   '1993-11-08'),
            ('Tomas Blaho',      'tomas.blaho@gmail.com',    '0918 333 221', 'Partizanska 45, Zilina',        '4012 8888 8888 1881', '1988-01-30'),
            ('Lucia Fialova',    'lucia.fialova@gmail.com',     '0905 741 852', 'Stefanikova 2, Trnava',         '6011 1111 1117 5556', '1995-06-19'),
            ('Jana Kovacova',    'jana.kovacova@email.sk',    '0911 123 456', 'Hlavna 12, Bratislava',        '4111 1111 1111 1111', '1990-03-15'),
            ('Peter Novak',      'peter.novak@gmail.com',     '0944 987 654', 'Namestie SNP 3, Banska Bystrica', '5500 0055 5555 5559', '1985-07-22'),
            ('Maria Horvathova', 'maria.horvath@post.sk',     '0902 555 777', 'Obchodna 8, Kosice',            '3714 496353 98431',   '1993-11-08'),
            ('Tomas Blaho',      'tomas.blaho@centrum.sk',    '0918 333 221', 'Partizanska 45, Zilina',        '4012 8888 8888 1881', '1988-01-30'),
            ('Jana Kovacova',    'jana.jana@email.sk',    '0911 123 456', 'Hlavna 12, Bratislava',        '4111 1111 1111 1111', '1990-03-15'),
            ('Peter Novak',      'peter.peter@gmail.com',     '0944 987 654', 'Namestie SNP 3, Banska Bystrica', '5500 0055 5555 5559', '1985-07-22'),
            ('Maria Horvathova', 'maria.ho@gmail.com',     '0902 555 777', 'Obchodna 8, Kosice',            '3714 496353 98431',   '1993-11-08'),
            ('Tomas Blaho',      'tomas.blaho@gmail.com',    '0918 333 221', 'Partizanska 45, Zilina',        '4012 8888 8888 1881', '1988-01-30'),
            ('Jana Kovacova',    'jana.jana@email.sk',    '0911 123 456', 'Hlavna 12, Bratislava',        '4111 1111 1111 1111', '1990-03-15'),
            ('Peter Novak',      'peter.peter@gmail.com',     '0944 987 654', 'Namestie SNP 3, Banska Bystrica', '5500 0055 5555 5559', '1985-07-22'),
            ('Maria Horvathova', 'maria.ho@gmail.com',     '0902 555 777', 'Obchodna 8, Kosice',            '3714 496353 98431',   '1993-11-08'),
            ('Tomas Blaho',      'tomas.blaho@gmail.com',    '0918 333 221', 'Partizanska 45, Zilina',        '4012 8888 8888 1881', '1988-01-30'),
            ('Lucia Fialova',    'lucia.fialova@azet.sk',     '0905 741 852', 'Stefanikova 2, Trnava',         '6011 1111 1117 5556', '1995-06-19');

        INSERT INTO orders (customer_id, product_id, order_date, quantity) VALUES
            (1, 1, '2024-11-03', 1),
            (2, 3, '2024-11-15', 1),
            (3, 5, '2024-12-01', 1),
            (4, 2, '2025-01-10', 1),
            (5, 7, '2025-02-22', 2),
            (1, 4, '2025-03-05', 1),
            (3, 8, '2025-03-18', 1);
    """)
    conn.commit()
    conn.close()
