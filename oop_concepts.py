"""
OOP Concepts Practice
----------------------
Covers: class vs instance attributes, name-mangled "private" attributes
with getter/setter, @property, @classmethod, and single inheritance
with super().
"""


class Student:
    college = "NITJ"          # class attribute, shared by all instances
    count = 0                 # tracks how many Student objects exist

    def __init__(self, name, age=18):
        self.name = name       # instance attribute
        self._age = age
        self.__cgpa = 0.0      # name-mangled "private" attribute
        Student.count += 1

    # --- getter/setter style access to a "private" attribute ---
    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self, value):
        if 0 <= value <= 10:
            self.__cgpa = value
        else:
            print("Invalid CGPA")

    # --- same idea, but using @property (more Pythonic) ---
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value

    @classmethod
    def show_college(cls):
        print(cls.college)

    @classmethod
    def total_students(cls):
        return cls.count


class Animal:
    def __init__(self):
        self.age = 10

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.breed = "Labrador"

    def speak(self):
        super().speak()
        print("Dog barks")


# Duck typing example: no shared base class needed
class Person:
    def quack(self):
        print("Humans quack too")


class Duck:
    def quack(self):
        print("Quack quack")


def make_sound(x):
    x.quack()


if __name__ == "__main__":
    s1 = Student("Aditya")
    s2 = Student("Rahul")
    s3 = Student("Ajay")

    Student.show_college()
    print("Total students:", Student.total_students())

    s1.set_cgpa(9.1)
    print(f"{s1.name}'s CGPA:", s1.get_cgpa())

    s1.age = 20
    print(f"{s1.name}'s age:", s1.age)

    print("\n--- Inheritance ---")
    d = Dog()
    d.speak()
    print("Dog's age (inherited):", d.age)

    print("\n--- Duck typing ---")
    make_sound(Person())
    make_sound(Duck())
