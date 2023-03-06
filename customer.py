from person import Person


class Customer(Person):  # subclass
    def __init__(self, name, gender, company):
        super().__init__(name, gender)
        # self.name = name
        # self.gender = gender
        self.company = company

    def __str__(self):
        return "Name: " + self.name + ", Gender: " + self.gender + ", Company: " + self.company

    def deadline(self, date):
        return f"The {self.company} project deadline is {date}."