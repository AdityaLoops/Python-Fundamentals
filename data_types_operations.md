# Python Data Types — All Operations Reference

A quick-reference guide to operations and methods for every core Python data type.

---

## 1. Numbers (int, float)

### Arithmetic Operations
```python
a, b = 10, 3

a + b      # Addition -> 13
a - b      # Subtraction -> 7
a * b      # Multiplication -> 30
a / b      # Division (float) -> 3.333...
a // b     # Floor division -> 3
a % b      # Modulus (remainder) -> 1
a ** b     # Exponent -> 1000
```

### Comparison Operations
```python
a == b     # Equal
a != b     # Not equal
a > b, a < b, a >= b, a <= b
```

### Useful Built-in Functions
```python
abs(-5)         # 5 (absolute value)
round(3.567, 2) # 3.57 (rounding)
pow(2, 3)       # 8 (same as 2**3)
divmod(10, 3)   # (3, 1) -> (quotient, remainder)
int(3.9)        # 3 (convert to int)
float(5)        # 5.0 (convert to float)
```

### Bitwise Operations (int only)
```python
a & b   # AND
a | b   # OR
a ^ b   # XOR
~a      # NOT
a << 1  # Left shift
a >> 1  # Right shift
```

---

## 2. Strings (str)

Strings are **immutable** — operations return a new string, they don't modify in place.

### Basic Operations
```python
s = "Hello World"

s + "!"           # Concatenation -> "Hello World!"
s * 2             # Repetition -> "Hello WorldHello World"
len(s)            # Length -> 11
s[0]              # Indexing -> "H"
s[-1]             # Last char -> "d"
s[0:5]            # Slicing -> "Hello"
s[::-1]           # Reverse -> "dlroW olleH"
"H" in s          # Membership -> True
```

### Common Methods
```python
s.lower()          # "hello world"
s.upper()          # "HELLO WORLD"
s.strip()          # removes leading/trailing whitespace
s.replace("World", "Python")  # "Hello Python"
s.split(" ")       # ['Hello', 'World']
"-".join(["a","b","c"])  # "a-b-c"
s.find("World")    # index of substring -> 6
s.count("o")       # count occurrences -> 2
s.startswith("Hello")  # True
s.endswith("World")    # True
s.isdigit()        # checks if all chars are digits
s.isalpha()        # checks if all chars are letters
s.title()          # "Hello World" (title case)
s.capitalize()     # capitalizes first letter only
f"{s} - formatted"  # f-string formatting

# Less common but handy
s.zfill(15)         # pads with zeros on the left to reach given length -> "0000Hello World"
s.ljust(20, "-")    # left-justify, pad right with char -> "Hello World---------"
s.rjust(20, "-")    # right-justify, pad left with char -> "---------Hello World"
s.swapcase()        # swaps upper/lower case -> "hELLO wORLD"
s.isalnum()         # True if all chars are letters/digits (no spaces/symbols)
s.isupper()         # True if all cased chars are uppercase
s.islower()         # True if all cased chars are lowercase
```

---

## 3. Lists (list) — mutable, ordered

### Basic Operations
```python
lst = [1, 2, 3, 4]

lst + [5, 6]     # Concatenation -> [1,2,3,4,5,6]
lst * 2          # Repetition
len(lst)         # Length
lst[0]           # Indexing
lst[1:3]         # Slicing -> [2, 3]
3 in lst         # Membership -> True
```

### Modifying Methods
```python
lst.append(5)         # Add single item at end
lst.extend([6, 7])    # Add multiple items at end
lst.insert(1, 99)     # Insert at index
lst.remove(99)        # Remove first matching value
lst.pop()             # Remove & return last item
lst.pop(0)            # Remove & return item at index
lst.clear()           # Empty the list
```

### Ordering & Info
```python
lst.sort()            # Sort in place (ascending)
lst.sort(reverse=True) # Descending
sorted(lst)           # Returns new sorted list (original untouched)
lst.reverse()         # Reverse in place
lst.index(3)          # Find index of value
lst.count(2)          # Count occurrences of value
lst.copy()            # Shallow copy
```

### List Comprehension
```python
squares = [x**2 for x in range(5)]         # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2==0] # filter with comprehension
```

### Shallow Copy vs Deep Copy
```python
import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()        # or list(original) or original[:]
deep = copy.deepcopy(original)

shallow[0].append(99)   # This ALSO changes original! (inner lists are shared references)
# original is now [[1, 2, 99], [3, 4]]

deep[1].append(100)     # This does NOT affect original (fully independent copy)
```
**Key point:** Shallow copy duplicates the outer list only — nested objects (like inner lists) are still shared references. Deep copy duplicates everything recursively, so nested objects are fully independent too.

---

## 4. Tuples (tuple) — immutable, ordered

Since tuples are immutable, they have far fewer methods than lists.

```python
t = (1, 2, 3, 2)

t[0]           # Indexing
t[1:3]         # Slicing
len(t)         # Length
t.count(2)     # Count occurrences -> 2
t.index(3)     # Find index of value -> 2
t + (4, 5)     # Concatenation -> (1,2,3,2,4,5)
t * 2          # Repetition

# Tuple unpacking
a, b, c, d = t
```

**Key point:** Use tuples when data shouldn't change (fixed records, coordinates, dictionary keys).

---

## 5. Dictionaries (dict) — mutable, key-value pairs

```python
d = {"name": "Aditya", "age": 20}

d["name"]              # Access value -> "Aditya"
d.get("age")            # Safer access (returns None if missing)
d.get("city", "N/A")    # Default value if key missing
d["city"] = "Jalandhar" # Add/update key
del d["age"]            # Delete key
d.pop("city")           # Remove & return value

d.keys()        # dict_keys(['name'])
d.values()      # dict_values(['Aditya'])
d.items()       # dict_items([('name','Aditya')])

"name" in d     # Membership check on KEYS
d.update({"age": 21})  # Merge/update dict
d.copy()        # Shallow copy
d.clear()       # Empty the dict

# Dict comprehension
squares = {x: x**2 for x in range(5)}

# Less common but handy
dict.fromkeys(["a", "b", "c"], 0)   # Creates dict with given keys, same default value -> {'a':0,'b':0,'c':0}
d.setdefault("age", 25)              # Returns value if key exists; if not, inserts key with given default
```

---

## 6. Sets (set) — mutable, unordered, no duplicates

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(4)             # Add single element
s1.update([5, 6])     # Add multiple elements
s1.remove(2)          # Remove (error if not found)
s1.discard(10)        # Remove (no error if not found)
s1.pop()              # Remove random element
s1.clear()            # Empty the set

# Set operations (very useful in DSA!)
s1 | s2    # Union
s1 & s2    # Intersection
s1 - s2    # Difference
s1 ^ s2    # Symmetric difference (in either, not both)

s1.issubset(s2)      # Check if subset
s1.issuperset(s2)    # Check if superset
```

**Key point:** Sets are great for removing duplicates and fast membership checks (`in` is O(1) average).

---

## 7. Booleans (bool)

```python
True, False

not True        # False
True and False  # False
True or False   # True

bool(0)      # False
bool(1)      # True
bool("")     # False (empty string is falsy)
bool("hi")   # True
bool([])     # False (empty list is falsy)
bool(None)   # False
```

---

## Quick Comparison Table

| Type   | Mutable? | Ordered? | Duplicates? | Indexed? |
|--------|----------|----------|-------------|----------|
| list   | Yes      | Yes      | Yes         | Yes      |
| tuple  | No       | Yes      | Yes         | Yes      |
| dict   | Yes      | Yes (3.7+) | Keys: No  | By key   |
| set    | Yes      | No       | No          | No       |
| str    | No       | Yes      | Yes         | Yes      |

---

