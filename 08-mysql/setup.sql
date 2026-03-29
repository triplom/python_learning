-- Setup SQL — Python Learning MySQL Lab
-- Course 1 §5

-- ─── Database ─────────────────────────────────────────────────────────────────
CREATE DATABASE IF NOT EXISTS pythonlab;
USE pythonlab;

-- ─── Tables ───────────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS customers (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    email      VARCHAR(150) UNIQUE NOT NULL,
    city       VARCHAR(80),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    name     VARCHAR(100) NOT NULL,
    price    DECIMAL(10, 2) NOT NULL,
    stock    INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS orders (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id  INT NOT NULL,
    quantity    INT NOT NULL DEFAULT 1,
    order_date  DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id)  REFERENCES products(id)  ON DELETE RESTRICT
);

-- ─── Sample Data ──────────────────────────────────────────────────────────────

INSERT INTO customers (name, email, city) VALUES
    ('Alice Souza',    'alice@example.com',  'São Paulo'),
    ('Bob Lima',       'bob@example.com',    'Rio de Janeiro'),
    ('Carol Ferreira', 'carol@example.com',  'Curitiba'),
    ('David Nunes',    'david@example.com',  'Brasília'),
    ('Eva Martins',    'eva@example.com',    'Belo Horizonte');

INSERT INTO products (name, price, stock) VALUES
    ('Python Book',      79.90, 50),
    ('Mechanical Keyboard', 349.99, 20),
    ('USB Hub',          49.99, 100),
    ('Webcam HD',        199.90, 35),
    ('Monitor 24"',      1299.00, 10);

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
    (1, 1, 2, '2026-01-15'),
    (1, 3, 1, '2026-01-20'),
    (2, 2, 1, '2026-01-22'),
    (3, 4, 1, '2026-02-01'),
    (4, 5, 2, '2026-02-05'),
    (5, 1, 1, '2026-02-10'),
    (2, 3, 3, '2026-02-15');

-- ─── Useful Queries ───────────────────────────────────────────────────────────

-- All orders with customer and product names
-- SELECT c.name AS customer, p.name AS product, o.quantity, o.order_date
-- FROM orders o
-- JOIN customers c ON o.customer_id = c.id
-- JOIN products  p ON o.product_id  = p.id
-- ORDER BY o.order_date;

-- Total revenue per customer
-- SELECT c.name, SUM(p.price * o.quantity) AS total_spent
-- FROM orders o
-- JOIN customers c ON o.customer_id = c.id
-- JOIN products  p ON o.product_id  = p.id
-- GROUP BY c.name
-- ORDER BY total_spent DESC;
