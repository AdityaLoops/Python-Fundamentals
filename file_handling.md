# Python — File Handling Reference

## Opening a File
```python
f = open("data.txt", "r")   # mode, see table below
f.close()

# Preferred: context manager, auto-closes file
with open("data.txt", "r") as f:
    content = f.read()
```

## File Modes
| Mode | Meaning |
|---|---|
| `"r"` | Read (default). Errors if file doesn't exist |
| `"w"` | Write. Creates file if missing, **overwrites** if exists |
| `"a"` | Append. Creates file if missing, adds to end if exists |
| `"x"` | Create. Errors if file already exists |
| `"r+"` | Read and write |
| `"rb"`, `"wb"`, `"ab"` | Same as above but binary mode |
| `"rt"`, `"wt"` | Text mode (default, usually omitted) |

## Reading
```python
with open("data.txt", "r") as f:
    content = f.read()          # entire file as one string
    
with open("data.txt", "r") as f:
    line = f.readline()         # single line (includes \n)

with open("data.txt", "r") as f:
    lines = f.readlines()       # list of all lines (each includes \n)

with open("data.txt", "r") as f:
    for line in f:               # memory-efficient line-by-line iteration
        print(line.strip())      # strip() removes trailing \n
```

## Writing
```python
with open("out.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Second line\n")

with open("out.txt", "w") as f:
    lines = ["line1\n", "line2\n", "line3\n"]
    f.writelines(lines)          # no automatic \n added

with open("out.txt", "a") as f:
    f.write("Appended line\n")   # doesn't erase existing content
```

## File Pointer / Position
| Function | Description |
|---|---|
| `f.tell()` | Current position in file (byte offset) |
| `f.seek(offset, whence)` | Move pointer. `whence`: 0=start, 1=current, 2=end |
| `f.seek(0)` | Go back to start of file |

```python
with open("data.txt", "r") as f:
    print(f.tell())      # 0
    f.read(5)             # read first 5 chars
    print(f.tell())       # 5
    f.seek(0)             # reset to start
```

## Checking File / Path (`os`, `os.path`, `pathlib`)
```python
import os

os.path.exists("data.txt")     # True/False
os.path.isfile("data.txt")     # True if it's a file
os.path.isdir("mydir")         # True if it's a directory
os.path.getsize("data.txt")    # size in bytes
os.remove("data.txt")          # delete file
os.rename("old.txt", "new.txt")
os.listdir(".")                # list files in current dir

# Modern alternative: pathlib
from pathlib import Path
p = Path("data.txt")
p.exists()
p.is_file()
p.stat().st_size
p.unlink()                      # delete
```

## Working with CSV (`csv` module)
```python
import csv

# Reading
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)              # list of strings

# Reading as dict
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["column_name"])

# Writing
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerows([["Aditya", 20], ["Rahul", 21]])

# Writing dict rows
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
    writer.writeheader()
    writer.writerow({"Name": "Aditya", "Age": 20})
```

## Working with JSON (`json` module)
```python
import json

# Read JSON file into Python dict/list
with open("data.json", "r") as f:
    data = json.load(f)

# Write Python object to JSON file
with open("out.json", "w") as f:
    json.dump(data, f, indent=4)

# String <-> object conversions (no file involved)
json_str = json.dumps({"a": 1})     # dict -> string
obj = json.loads(json_str)          # string -> dict
```

## Binary Files
```python
with open("image.png", "rb") as f:
    data = f.read()               # bytes object

with open("copy.png", "wb") as f:
    f.write(data)
```

## Useful Patterns
```python
# Count lines in a file
with open("data.txt") as f:
    count = sum(1 for _ in f)

# Read file into a list, stripped
with open("data.txt") as f:
    lines = [line.strip() for line in f]

# Word frequency count
with open("data.txt") as f:
    text = f.read().split()
    from collections import Counter
    freq = Counter(text)

# Safely check before opening
import os
if os.path.exists("data.txt"):
    with open("data.txt") as f:
        print(f.read())
```

## Notes
- Always prefer `with open(...)` — it auto-closes the file even if an exception occurs.
- Use `newline=""` when writing CSVs on Windows to avoid extra blank lines.
- Mixing `"r+"` reads and writes can be tricky with pointer position — use `seek()` carefully.
