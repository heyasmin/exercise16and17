class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}"
