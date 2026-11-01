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
        DROP TABLE IF EXISTS prod;
        DROP TABLE IF EXISTS users;

        CREATE TABLE prod (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            price REAL NOT NULL,
            desc  TEXT
        );

        CREATE TABLE users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role     TEXT DEFAULT 'user'
        );

        CREATE TABLE customers (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            f_name        TEXT NOT NULL,
            last_name     TEXT NOT NULL,
            email         TEXT NOT NULL,
            phone         TEXT,
            address       TEXT,
            credit_card   TEXT,
            date_of_birth TEXT
        );

        CREATE TABLE orders (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            product_id  INTEGER NOT NULL,
            order_date  TEXT NOT NULL,
            quantity    INTEGER DEFAULT 1,
            FOREIGN KEY (customer_id) REFERENCES customers(id),
            FOREIGN KEY (product_id)  REFERENCES prod(id)
        );

        INSERT INTO prod (name, price, desc) VALUES
            ('Kocik Maxi Cosi Zelia',        290.00,  'lahky kombi kocik 3v1'),
            ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
             ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
             ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
             ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
             ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
             ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
            ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'), ('Kocik Bugaboo Fox 5',          1200.00, 'premiovy kocik odpruzeny podvozok mega top stav radsej osobny odber'),
             ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'), ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'), ('Kocik Joie Mytrax Flex',        450.00, 'skladaci kocik s otocnou sedackou'),
            ('Kocik Chicco Trio Best Friend', 350.00,  'trio system autosedacka chicco'),
            ('Kocik Silver Cross Wave',       890.00,  'tandem pre 2 deti'),
            ('Kocik Cybex Balios S Lux',      750.00,  'reverzibilna sedacka od narodenia do 22 kg malo pouzivany bez poskodeni'),
            ('Kocik Thule Spring',            500.00,  'lahky mestsky kocik'),
            ('Kocik Hauck Rapid 4',           190.00,  'ekonomicky kocik nastavitelna opierka chrbta radsej do mesta');

        INSERT INTO users (username, password, role) VALUES
            ('admin', 'tajneheslo123', 'admin'),
            ('jan',   'heslo456',      'user'),
            ('palo1',  'heslo456',      'user'),
            ('marek1', 'heslo456',      'user'),
            ('hetes1', 'heslo456',      'user'),
            ('juro1',  'heslo456',      'user'),
            ('palo',  'heslo456',      'user'),
            ('marek', 'heslo456',      'user'),
            ('hetes', 'heslo456',      'user'),
            ('juro',  'heslo456',      'user'),
            ('peto',  'heslo456',      'user'),
            ('milan', 'heslo456',      'user');

        INSERT INTO customers (f_name, last_name, email, phone, address, credit_card, date_of_birth) VALUES
            ('Jana',   'Kovacova',    'jana.kovacova@email.sk',      '0911 123 456', 'Hlavna 12, Bratislava',            '4111 1111 1111 1111', '1990-03-15'),
            ('Peter',  'Novak',       'peter.novak@gmail.com',       '0944 987 654', 'Namestie SNP 3, Banska Bystrica',  '5500 0055 5555 5559', '1985-07-22'),
            ('Maria',  'Horvathova',  'maria.horvath@post.sk',       '0902 555 777', 'Obchodna 8, Kosice',               '3714 496353 98431',   '1993-11-08'),
            ('Tomas',  'Blaho',       'tomas.blaho@centrum.sk',      '0918 333 221', 'Partizanska 45, Zilina',           '4012 8888 8888 1881', '1988-01-30'),
            ('Lucia',  'Fialova',     'lucia.fialova@azet.sk',       '0905 741 852', 'Stefanikova 2, Trnava',            '6011 1111 1117 5556', '1995-06-19'),
            ('Martin', 'Kral',        'martin.kral@gmail.com',       '0907 654 321', 'Kolarska 7, Nitra',                '4532 1234 5678 9012', '1991-09-04'),
            ('Zuzana', 'Prochazkova', 'zuzana.prochazka@zoznam.sk',  '0903 112 998', 'Mierova 33, Presov',               '5425 2334 3010 9903', '1987-12-27');

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
