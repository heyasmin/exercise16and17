from person import Person


class Employee(Person):  # subclass
    def __init__(self, name, gender, role):
        super().__init__(name, gender)
        # self.name = name
        # self.gender = gender
        self.role = role

    def __str__(self):
        return "Name: " + self.name + ", Gender: " + self.gender + ", Position: " + self.role

    def get_tasks(self, tasks):
        return f"{self.name} has completed {tasks} tasks from the project."

    # add setter/getter as employees can work on all projects, in the constructor
