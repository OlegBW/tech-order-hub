CREATE TABLE product(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	product_name TEXT UNIQUE,
    price REAL,
    creation_date TIMESTAMP
);

CREATE TABLE employee(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    user_name TEXT UNIQUE,
    email TEXT UNIQUE,
    hashed_password TEXT UNIQUE,
    user_role TEXT
);

CREATE TABLE order_info(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id REFERENCES product(id) ON UPDATE CASCADE ON DELETE CASCADE,
    cashier_id REFERENCES employee(id) ON UPDATE CASCADE ON DELETE CASCADE,
    order_status TEXT,
    order_date TIMESTAMP,
    discount REAL
);