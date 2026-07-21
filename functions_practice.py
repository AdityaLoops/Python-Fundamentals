"""
Function Practice
------------------
Small self-contained exercises: max of two values, even/odd check,
factorial (iterative + recursive), *args averaging, vowel counting,
and merging dictionaries.
"""


def maxi(a, b):
    return max(a, b)


def is_even(n):
    return n % 2 == 0


def factorial_iterative(n):
    fac = n
    while n > 1:
        n -= 1
        fac *= n
    return fac


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def average(*nums):
    return sum(nums) / len(nums)


def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count


def merge_dicts(d1, d2):
    return d1 | d2


if __name__ == "__main__":
    print("Max of 6 and 6.9:", maxi(6, 6.9))

    print("Is 8 even?", is_even(8))
    print("Is 7 even?", is_even(7))

    print("5! (iterative):", factorial_iterative(5))
    print("5! (recursive):", factorial_recursive(5))

    print("Average of 1-6:", average(1, 2, 3, 4, 5, 6))

    print("Vowel count:", count_vowels("this is a lovely day"))

    d1 = {1: 2, 2: 3, 4: 7}
    d2 = {4: 8, 7: 9, 8: 9}
    print("Merged dicts:", merge_dicts(d1, d2))
