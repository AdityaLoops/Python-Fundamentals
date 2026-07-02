# loops practice - while, for, range(), nested loops

def print_range_while(n):
    # basic while loop
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1
    print()

def print_even_numbers(n):
    # for loop with range, step of 2
    for i in range(2, n+1, 2):
        print(i, end=" ")
    print()

def print_multiplication_table(n):
    # nested loop for tables
    for i in range(1, n+1):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("-"*15)

def print_pyramid(rows):
    # just a simple star pattern, nested loop practice
    for i in range(1, rows+1):
        print("*"*i)


print("numbers 1 to 10:")
print_range_while(10)

print("\neven numbers up to 20:")
print_even_numbers(20)

print("\nmultiplication table for 3:")
print_multiplication_table(3)

print("\npyramid:")
print_pyramid(5)
