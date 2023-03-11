from employee import Employee
from customer import Customer

manager = Employee('Pam', 'F', 'Software Manager')
senior = Employee('Mirfat', 'F', 'Scrum Master')
junior = Employee('Eyasmin', 'F', 'Junior Engineer')

print(manager, senior, junior, sep='\n',)
print('/' * 20)

netflix = Customer('Michael', 'M', 'Netflix')
apple = Customer('Steve', 'M', 'Apple')
barclays = Customer('Laura', 'F', 'Barclays')
print(netflix, apple, barclays, sep="\n")
print('/' * 20)


print(netflix.deadline('20th of March 2023'))
print(junior.tasks(5))
