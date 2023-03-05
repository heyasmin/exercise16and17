# notes
# encapsulation: data and programs are hidden
# inheritance: a class can derive methods and properties from another class
# polymorphism: different subclasses of the same superclass, can implement their shared interface

# the constructor
class Person:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender.upper()

    def __str__(self):
        return "Name: " + self._name + \
            " Gender: " + self._gender
