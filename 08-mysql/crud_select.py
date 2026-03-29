# MySQL CRUD with Python — SELECT
# Course 1 §6
# Requires: pip install mysql-connector-python
# Start DB: docker compose up -d (in 08-mysql/)

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "labuser",
    "password": "labpass",
    "database": "pythonlab",
}


def get_connection():
    """Return a new database connection."""
    return mysql.connector.connect(**DB_CONFIG)


# ─── SELECT all customers ─────────────────────────────────────────────────────
def select_all_customers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # returns rows as dicts
    try:
        cursor.execute("SELECT * FROM customers ORDER BY name")
        rows = cursor.fetchall()
        print(f"\n{'ID':<4} {'Name':<20} {'City':<20} {'Email'}")
        print("-" * 65)
        for row in rows:
            print(
                f"{row['id']:<4} {row['name']:<20} {row['city'] or '':<20} {row['email']}"
            )
        return rows
    finally:
        cursor.close()
        conn.close()


# ─── SELECT with WHERE ────────────────────────────────────────────────────────
def find_customer_by_city(city):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        # Use parameterized query — NEVER use string formatting (SQL injection risk)
        cursor.execute("SELECT * FROM customers WHERE city = %s ORDER BY name", (city,))
        rows = cursor.fetchall()
        print(f"\nCustomers in {city}:")
        for row in rows:
            print(f"  {row['id']}: {row['name']} <{row['email']}>")
        return rows
    finally:
        cursor.close()
        conn.close()


# ─── JOIN query ───────────────────────────────────────────────────────────────
def get_orders_with_details():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
            SELECT
                o.id          AS order_id,
                c.name        AS customer,
                p.name        AS product,
                o.quantity,
                p.price,
                (p.price * o.quantity) AS subtotal,
                o.order_date
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            JOIN products  p ON o.product_id  = p.id
            ORDER BY o.order_date DESC
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(
            f"\n{'Order':<7} {'Customer':<18} {'Product':<22} {'Qty':<5} {'Subtotal':>10} {'Date'}"
        )
        print("-" * 75)
        for row in rows:
            print(
                f"{row['order_id']:<7} {row['customer']:<18} {row['product']:<22} "
                f"{row['quantity']:<5} R${row['subtotal']:>8.2f}  {row['order_date']}"
            )
        return rows
    finally:
        cursor.close()
        conn.close()


# ─── Aggregate query ──────────────────────────────────────────────────────────
def revenue_per_customer():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        sql = """
            SELECT c.name, SUM(p.price * o.quantity) AS total_spent
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
            JOIN products  p ON o.product_id  = p.id
            GROUP BY c.name
            ORDER BY total_spent DESC
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print("\nRevenue per customer:")
        for row in rows:
            print(f"  {row['name']:<20} R${row['total_spent']:>10.2f}")
        return rows
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    try:
        select_all_customers()
        find_customer_by_city("São Paulo")
        get_orders_with_details()
        revenue_per_customer()
    except Error as e:
        print(f"Database error: {e}")
        print("Make sure the MySQL container is running: docker compose up -d")
