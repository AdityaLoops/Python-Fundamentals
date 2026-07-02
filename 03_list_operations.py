# list operations - indexing, slicing, methods, enumerate

def slicing_demo():
    nums = [10, 20, 30, 40, 50, 60, 70]
    print("original:", nums)
    print("first three:", nums[:3])
    print("last three:", nums[-3:])
    print("reversed:", nums[::-1])
    print("every second element:", nums[::2])


def list_methods_demo():
    fruits = ["apple", "banana", "cherry"]
    print("start:", fruits)

    fruits.append("date")
    print("after append:", fruits)

    fruits.insert(1, "blueberry")
    print("after insert at index 1:", fruits)

    fruits.remove("banana")
    print("after remove banana:", fruits)

    popped = fruits.pop()
    print("after pop:", fruits, "| popped:", popped)

    fruits.sort()
    print("after sort:", fruits)

    fruits.reverse()
    print("after reverse:", fruits)

    print("index of cherry:", fruits.index("cherry"))
    print("count of apple:", fruits.count("apple"))


def enumerate_demo():
    subjects = ["Python", "DSA", "DBMS", "VLSI"]
    for index, subject in enumerate(subjects, start=1):
        print(index, subject)


def sorted_vs_sort_demo():
    marks = [88, 45, 67, 92, 33]
    sorted_marks = sorted(marks)  # doesnt change original list
    print("original:", marks)
    print("sorted() result:", sorted_marks)

    marks.sort(reverse=True)  # this one changes it in place
    print("after .sort(reverse=True):", marks)


print("--- slicing ---")
slicing_demo()

print("\n--- list methods ---")
list_methods_demo()

print("\n--- enumerate ---")
enumerate_demo()

print("\n--- sorted vs sort ---")
sorted_vs_sort_demo()
