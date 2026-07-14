# Python — SQLite Database Connection Reference (`sqlite3`)

`sqlite3` is built into Python's standard library — no installation needed.

## Basic Connection Flow
```python
import sqlite3

conn = sqlite3.connect("mydatabase.db")   # creates file if it doesn't exist
cursor = conn.cursor()

# ... run queries ...

conn.commit()    # save changes
conn.close()     # close connection
```

## Using with-statement (auto-commit on success, but does NOT auto-close)
```python
import sqlite3

with sqlite3.connect("mydatabase.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES ('Aditya')")
    # commits automatically at end of block if no exception
conn.close()   # still need to close manually
```

## In-memory Database (useful for testing)
```python
conn = sqlite3.connect(":memory:")   # temporary DB, gone when connection closes
```

## Creating a Table
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
""")
conn.commit()
```

## Inserting Data
```python
# Single insert — always use placeholders (?) to prevent SQL injection
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
               ("Aditya", 20, "aditya@example.com"))
conn.commit()

# NEVER do this (vulnerable to SQL injection):
# cursor.execute(f"INSERT INTO users (name) VALUES ('{name}')")

# Bulk insert
users = [
    ("Rahul", 21, "rahul@example.com"),
    ("Priya", 22, "priya@example.com"),
]
cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users)
conn.commit()

# Get the last inserted row's id
print(cursor.lastrowid)
```

## Reading Data (SELECT)
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()          # list of tuples, all rows
for row in rows:
    print(row)                    # (1, 'Aditya', 20, 'aditya@example.com')

cursor.execute("SELECT * FROM users WHERE age > ?", (20,))
row = cursor.fetchone()           # single row (or None)

cursor.execute("SELECT * FROM users")
first_three = cursor.fetchmany(3) # limited number of rows

# Iterating directly over cursor (memory efficient, no fetchall needed)
cursor.execute("SELECT name, age FROM users")
for name, age in cursor:
    print(name, age)
```

## Updating Data
```python
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (23, "Aditya"))
conn.commit()
print(cursor.rowcount)   # number of rows affected
```

## Deleting Data
```python
cursor.execute("DELETE FROM users WHERE name = ?", ("Rahul",))
conn.commit()
```

## Getting Column Names / Row as Dict
```python
conn = sqlite3.connect("mydatabase.db")
conn.row_factory = sqlite3.Row     # makes rows accessible like dicts
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row["name"], row["age"])   # access by column name
    print(dict(row))                  # convert to actual dict
```

## Transactions & Rollback
```python
try:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Test", 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Test2", None))
    conn.commit()
except sqlite3.Error as e:
    print("Error occurred:", e)
    conn.rollback()    # undo changes made since last commit
```

## Handling Errors
```python
import sqlite3

try:
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Aditya", "aditya@example.com"))
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Constraint violated (e.g. duplicate UNIQUE value):", e)
except sqlite3.OperationalError as e:
    print("SQL syntax or table doesn't exist:", e)
except sqlite3.Error as e:
    print("General SQLite error:", e)
finally:
    conn.close()
```

## Useful Table Introspection
```python
# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

# Get schema of a table
cursor.execute("PRAGMA table_info(users)")
for col in cursor.fetchall():
    print(col)   # (cid, name, type, notnull, default_value, pk)
```

## Common SQL Clauses Used with `execute()`
| Clause | Example |
|---|---|
| `WHERE` | `SELECT * FROM users WHERE age > 18` |
| `ORDER BY` | `SELECT * FROM users ORDER BY age DESC` |
| `LIMIT` | `SELECT * FROM users LIMIT 5` |
| `LIKE` | `SELECT * FROM users WHERE name LIKE 'A%'` |
| `JOIN` | `SELECT u.name, o.item FROM users u JOIN orders o ON u.id = o.user_id` |
| `GROUP BY` | `SELECT age, COUNT(*) FROM users GROUP BY age` |
| `DISTINCT` | `SELECT DISTINCT age FROM users` |

## Full Example — Small CRUD Script
```python
import sqlite3

def create_connection(db_file="app.db"):
    return sqlite3.connect(db_file)

def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks INTEGER
        )
    """)
    conn.commit()

def add_student(conn, name, marks):
    conn.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
    conn.commit()

def get_all_students(conn):
    cursor = conn.execute("SELECT * FROM students")
    return cursor.fetchall()

def update_marks(conn, name, marks):
    conn.execute("UPDATE students SET marks = ? WHERE name = ?", (marks, name))
    conn.commit()

def delete_student(conn, name):
    conn.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()

if __name__ == "__main__":
    conn = create_connection()
    create_table(conn)
    add_student(conn, "Aditya", 95)
    add_student(conn, "Rahul", 88)
    print(get_all_students(conn))
    update_marks(conn, "Rahul", 90)
    delete_student(conn, "Aditya")
    conn.close()
```

## Notes
- Always use `?` placeholders instead of f-strings/`%` formatting in queries — prevents SQL injection.
- `conn.commit()` is required after INSERT/UPDATE/DELETE, or changes won't persist.
- `cursor.execute()` and `conn.execute()` (shortcut on connection object) both work — the latter creates a temporary cursor internally.
- For bigger projects, consider an ORM like **SQLAlchemy**, but raw `sqlite3` is great for learning fundamentals and small scripts.
