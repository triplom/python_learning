# MySQL Cheatsheet

## Connection (mysql-connector-python)

```python
import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1", port=3306,
    user="labuser", password="labpass",
    database="pythonlab",
)
cursor = conn.cursor(dictionary=True)   # rows as dicts
```

## CRUD

```python
# SELECT
cursor.execute("SELECT * FROM users WHERE city = %s", ("São Paulo",))
rows = cursor.fetchall()     # list of dicts
row  = cursor.fetchone()     # single dict or None

# INSERT
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("Alice", "alice@example.com")
)
conn.commit()
new_id = cursor.lastrowid

# Batch INSERT
cursor.executemany(
    "INSERT INTO products (name, price) VALUES (%s, %s)",
    [("Book", 49.99), ("Pen", 2.99)]
)
conn.commit()

# UPDATE
cursor.execute(
    "UPDATE products SET price = %s WHERE id = %s",
    (59.99, 1)
)
conn.commit()

# DELETE
cursor.execute("DELETE FROM orders WHERE id = %s", (5,))
conn.commit()

# Cleanup
cursor.close()
conn.close()
```

## SQL Quick Reference

```sql
-- DDL
CREATE TABLE users (
    id    INT AUTO_INCREMENT PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

ALTER TABLE users ADD COLUMN city VARCHAR(80);
DROP TABLE users;

-- DML
SELECT * FROM users ORDER BY name LIMIT 10;
SELECT name, COUNT(*) FROM orders GROUP BY name HAVING COUNT(*) > 1;

-- JOIN
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.total > 100
ORDER BY o.total DESC;

-- Aggregation
SELECT dept, AVG(salary), MIN(salary), MAX(salary), COUNT(*)
FROM employees
GROUP BY dept;
```

## Docker MySQL Lab

```bash
cd 08-mysql
docker compose up -d          # start MySQL + Adminer
docker compose ps             # check status
docker compose exec mysql mysql -u labuser -plabpass pythonlab
docker compose down           # stop
docker compose down -v        # stop + delete data
```

**Adminer UI:** http://localhost:8080  
Server: `mysql` · User: `labuser` · Password: `labpass` · DB: `pythonlab`

## Best Practices

- Always use parameterized queries (`%s`) — never string formatting (SQL injection)
- Always `conn.commit()` after write operations
- Use `try/except/finally` to ensure `cursor.close()` and `conn.close()`
- Use `conn.rollback()` on exception to undo partial changes
