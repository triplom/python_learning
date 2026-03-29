# MySQL CRUD — INSERT, UPDATE, DELETE
# Course 1 §6

import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "labuser",
    "password": "labpass",
    "database": "pythonlab",
}


def get_conn():
    return mysql.connector.connect(**DB_CONFIG)


# ─── INSERT ───────────────────────────────────────────────────────────────────
def insert_customer(name, email, city=None):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO customers (name, email, city) VALUES (%s, %s, %s)",
            (name, email, city),
        )
        conn.commit()
        new_id = cursor.lastrowid
        print(f"Inserted customer ID={new_id}: {name}")
        return new_id
    except Error as e:
        conn.rollback()
        print(f"Insert failed: {e}")
        return None
    finally:
        cursor.close()
        conn.close()


def insert_many_products(products):
    """Batch insert with executemany()."""
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.executemany(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", products
        )
        conn.commit()
        print(f"Inserted {cursor.rowcount} products")
    except Error as e:
        conn.rollback()
        print(f"Batch insert failed: {e}")
    finally:
        cursor.close()
        conn.close()


# ─── UPDATE ───────────────────────────────────────────────────────────────────
def update_product_price(product_id, new_price):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE products SET price = %s WHERE id = %s", (new_price, product_id)
        )
        conn.commit()
        print(
            f"Updated product {product_id}: price → R${new_price:.2f} "
            f"({cursor.rowcount} row(s) affected)"
        )
    except Error as e:
        conn.rollback()
        print(f"Update failed: {e}")
    finally:
        cursor.close()
        conn.close()


def update_stock(product_id, delta):
    """Adjust stock by delta (positive=add, negative=reduce)."""
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE products SET stock = stock + %s WHERE id = %s AND stock + %s >= 0",
            (delta, product_id, delta),
        )
        conn.commit()
        if cursor.rowcount == 0:
            print(
                f"Stock update failed: product {product_id} not found or stock would go negative"
            )
        else:
            print(f"Stock updated for product {product_id}: Δ{delta:+d}")
    finally:
        cursor.close()
        conn.close()


# ─── DELETE ───────────────────────────────────────────────────────────────────
def delete_customer(customer_id):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM customers WHERE id = %s", (customer_id,))
        conn.commit()
        print(f"Deleted customer ID={customer_id} ({cursor.rowcount} row(s))")
    except Error as e:
        conn.rollback()
        print(f"Delete failed: {e}")
    finally:
        cursor.close()
        conn.close()


# ─── DEMO ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        # Insert
        new_id = insert_customer("Fernanda Costa", "fernanda@example.com", "Fortaleza")

        # Batch insert products
        new_products = [
            ("SSD 1TB", 399.90, 15),
            ("RAM 16GB", 249.99, 25),
        ]
        insert_many_products(new_products)

        # Update
        update_product_price(1, 89.90)  # Python Book price increase
        update_stock(3, -5)  # Sold 5 USB Hubs

        # Delete the test customer (cleanup)
        if new_id:
            delete_customer(new_id)

    except Error as e:
        print(f"Connection error: {e}")
        print("Run: docker compose up -d")
