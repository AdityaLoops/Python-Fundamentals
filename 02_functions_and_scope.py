# functions practice - default args, keyword args, scope

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def student_info(name, branch, year=1):
    print(f"Name: {name} | Branch: {branch} | Year: {year}")

counter = 0  # global var

def increment_global():
    global counter
    counter += 1

def local_scope_demo():
    # this counter is local, doesnt touch the global one
    counter = 100
    counter += 1
    print(f"inside function, local counter = {counter}")

def min_max(numbers):
    # returns both min and max at once
    return min(numbers), max(numbers)


greet("Aditya")
greet("Aditya", greeting="Hey")

student_info("Aditya", "ECE")
student_info(name="Aditya", branch="ECE", year=2)

print(f"\nglobal counter before: {counter}")
increment_global()
increment_global()
print(f"global counter after: {counter}")

local_scope_demo()
print(f"global counter still same: {counter}")

nums = [4, 8, 15, 16, 23, 42]
low, high = min_max(nums)
print(f"\nmin: {low}, max: {high}")
