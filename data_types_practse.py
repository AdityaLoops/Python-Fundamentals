# data_types_practice.py
# just running through all the data type stuff to make sure i actually get it


print("===== STRINGS =====")

s = "Hello World"
print(s.upper())                     # HELLO WORLD
print(s.lower())                     # hello world
print(s.replace("World", "Python"))  # Hello Python
print(s[::-1])                       # reversed -> dlroW olleH
print(s.split(" "))                  # ['Hello', 'World']
print("-".join(["a", "b", "c"]))     # a-b-c
print(s.find("World"))               # 6
print(s.count("o"))                  # 2
print(s.zfill(15))                   # 0000Hello World
print(s.ljust(20, "-"))
print(s.swapcase())                  # hELLO wORLD


print("\n===== NUMBERS =====")

a, b = 10, 3
print(a + b, a - b, a * b)
print(a / b)      # normal division
print(a // b)     # floor division
print(a % b)      # remainder
print(a ** b)     # power
print(divmod(a, b))  # (quotient, remainder) in one shot


print("\n===== LISTS =====")

lst = [1, 2, 3, 4]
lst.append(5)
lst.insert(1, 99)
print(lst)
lst.remove(99)
print(lst)
print(sorted(lst, reverse=True))   # doesn't touch original list
print([x**2 for x in range(5)])    # comprehension, gotta get comfortable with these

# shallow vs deep copy - the thing that always trips people up
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0].append(100)   # this changes original too! inner lists are shared
deep[1].append(200)      # this does NOT touch original

print("original:", original)
print("shallow:", shallow)
print("deep:", deep)


print("\n===== TUPLES =====")

t = (1, 2, 3, 2)
print(t.count(2))     # 2
print(t.index(3))     # 2
x, y, z, w = t         # unpacking, always feels satisfying
print(x, y, z, w)


print("\n===== DICTS =====")

d = {"name": "Aditya", "age": 20}
print(d.get("age"))
print(d.get("city", "not found"))  # avoids KeyError
d["city"] = "Jalandhar"
d.setdefault("age", 99)  # won't overwrite since age already exists
print(d)
print(dict.fromkeys(["x", "y", "z"], 0))


print("\n===== SETS =====")

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)   # union
print(s1 & s2)   # intersection - common elements
print(s1 - s2)   # what's only in s1
print(s1 ^ s2)   # symmetric diff - in either but not both


print("\n===== BOOLEANS =====")

print(bool(0), bool(1), bool(""), bool("hi"), bool([]))
print(True and False, True or False, not True)


# TODO: come back and add more edge cases once i learn OOP + error handling
