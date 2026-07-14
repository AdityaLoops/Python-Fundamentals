# Python — Exception Handling Reference

## Basic Structure
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Full try / except / else / finally
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Not a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Success, result =", result)   # runs only if no exception occurred
finally:
    print("This always runs")             # cleanup code, runs no matter what
```

## Catching Multiple Exceptions
```python
try:
    ...
except (ValueError, TypeError) as e:
    print("Caught:", e)

# Catch anything (use sparingly, hides real bugs)
try:
    ...
except Exception as e:
    print("Something went wrong:", e)
```

## Common Built-in Exceptions
| Exception | When it's raised |
|---|---|
| `ValueError` | Right type, invalid value (e.g. `int("abc")`) |
| `TypeError` | Operation on incompatible types |
| `ZeroDivisionError` | Division/modulo by zero |
| `IndexError` | List/tuple index out of range |
| `KeyError` | Dict key not found |
| `AttributeError` | Attribute/method doesn't exist on object |
| `FileNotFoundError` | File doesn't exist (subclass of `OSError`) |
| `IOError` / `OSError` | I/O operation failure |
| `ImportError` / `ModuleNotFoundError` | Module import fails |
| `NameError` | Variable not defined |
| `StopIteration` | Iterator has no more items |
| `RecursionError` | Max recursion depth exceeded |
| `MemoryError` | Out of memory |
| `KeyboardInterrupt` | User hits Ctrl+C |
| `AssertionError` | `assert` statement fails |
| `NotImplementedError` | Abstract method not implemented |
| `OverflowError` | Numeric result too large |

## Raising Exceptions
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Re-raising inside except (preserves original traceback)
try:
    risky()
except Exception as e:
    print("Logging error:", e)
    raise            # re-raise the same exception

# Raising from another exception (chaining, shows both tracebacks)
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Conversion failed") from e
```

## Custom Exceptions
```python
class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance."""
    def __init__(self, message="Insufficient balance"):
        self.message = message
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(f"Tried to withdraw {amount}, balance is {balance}")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientBalanceError as e:
    print(e)
```

## `assert` Statement
```python
def divide(a, b):
    assert b != 0, "b cannot be zero"
    return a / b

# assert is stripped out when Python runs with -O (optimized) flag
# so don't use it for critical runtime checks in production code
```

## Exception Object Attributes
```python
try:
    1 / 0
except ZeroDivisionError as e:
    print(type(e))          # <class 'ZeroDivisionError'>
    print(e.args)            # ('division by zero',)
    print(str(e))            # division by zero
```

## `with` Statement (Context Managers) — cleaner alternative to try/finally
```python
# Automatically handles cleanup (closing files, releasing locks, etc.)
with open("data.txt") as f:
    data = f.read()
# file is closed automatically, even if an exception occurs inside the block

# Custom context manager
class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False   # False = don't suppress exceptions

with Resource() as r:
    print("Using resource")
```

## Exception Hierarchy (simplified)
```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │     ├── ZeroDivisionError
      │     └── OverflowError
      ├── LookupError
      │     ├── IndexError
      │     └── KeyError
      ├── ValueError
      ├── TypeError
      ├── OSError
      │     └── FileNotFoundError
      └── ... (many more)
```
Catching a parent class (e.g. `LookupError`) also catches its subclasses (`IndexError`, `KeyError`).

## Common Patterns
```python
# Retry logic
for attempt in range(3):
    try:
        risky_operation()
        break
    except ConnectionError:
        print(f"Retrying... attempt {attempt + 1}")
else:
    print("All attempts failed")

# Validating input in a loop
while True:
    try:
        n = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input, try again")

# Cleanup guaranteed regardless of outcome
try:
    conn = open_connection()
    use_connection(conn)
except ConnectionError:
    print("Connection failed")
finally:
    conn.close()
```

## Notes
- Prefer specific exceptions over a bare `except:` — bare except also catches `KeyboardInterrupt` and `SystemExit`, which usually isn't what you want.
- `finally` always executes, even if `return` is hit inside `try` or `except`.
- Use custom exceptions to make error handling more meaningful in larger projects (e.g. your ML pipeline or DB code).
