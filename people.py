from employee import Employee
from customer import Customer

manager = Employee('Pam', 'f', 'Software Manager')
senior = Employee('Mirfat', 'f', 'Scrum Master')
junior = Employee('Eyasmin', 'f', 'Junior Engineer')

print(manager, senior, junior, sep='\n',)
print('/' * 20)

netflix = Customer('Michael', 'm', 'Netflix')
apple = Customer('Steve', 'm', 'Apple')
barclays = Customer('Laura', 'f', 'Barclays')
print(netflix, apple, barclays, sep="\n")

print(netflix.deadline('20th of March 2023.'))
