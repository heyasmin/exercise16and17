class Person:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    def __str__(self):
        return f"Name: {self._name}, Gender: {self._gender}"


class Employee(Person):  # subclass
    def __init__(self, name, gender, role):
        super().__init__(name, gender)
        # self._name = name
        # self._gender = gender
        self._role = role

    def __str__(self):
        return "Name: " + self._name + ", Gender: " + self._gender + ", Position: " + self._role

    def tasks(self, tasks):
        return f"{self._name} has completed {tasks} tasks from the project."


class Customer(Person):  # subclass
    def __init__(self, name, gender, company):
        super().__init__(name, gender)
        # self._name = name
        # self._gender = gender
        self._company = company

    def __str__(self):
        return "Name: " + self._name + ", Gender: " + self._gender + ", Company: " + self._company

    def deadline(self, date):
        return f"The {self._company} project deadline is {date}."


manager = Employee('Pam', 'F', 'Software Manager')
senior = Employee('Mirfat', 'F', 'Scrum Master')
junior = Employee('Eyasmin', 'F', 'Junior Engineer')

print(manager, senior, junior, sep='\n',)
print('/' * 20)

netflix = Customer('Michael', 'M', 'Netflix')
apple = Customer('Steve', 'M', 'Apple')
barclays = Customer('Laura', 'M', 'Barclays')
print(netflix, apple, barclays, sep="\n")

print(netflix.deadline('20th of March 2023'))
print(junior.tasks(5))