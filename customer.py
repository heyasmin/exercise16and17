from person import Person
# Customer inherits from superclass Person
# a customer is a type of person, so the properties derive from person(inheritance)


class Customer(Person):  # subclass
    def __init__(self, name, gender, company):
        super().__init__(name, gender)
        self._company = company

    def __str__(self):
        return "Name: " + self._name + \
            ", Gender: " + self._gender + \
            ", Company: " + self._company

    def deadline(self, date):
        return f"The {self._company} project deadline is {date}"
