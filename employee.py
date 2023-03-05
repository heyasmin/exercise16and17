from person import Person
# Employee inherits from superclass Person
# an employee is a type of person, so the properties derive from person (inheritance)


class Employee(Person):  # subclass
    def __init__(self, name, gender, role):
        super().__init__(name, gender)
        self._role = role

    def __str__(self):
        return "Name: " + self._name + \
            ", Gender: " + self._gender + \
            ", Position: " + self._role

    def bookholiday(self, days):
        return f"Employee has requested {days} days of holidays."

