class Account:

    def __init__(self, initial_amount):  # this is the constructor, it creates the object
        self._balance = initial_amount

    def deposit(self, amount):  # deposit is a method!
        self._balance += amount
        return f"You have deposited £{amount}."

    def get_balance(self):  # getter
        return self._balance

    def withdraw(self, amount):
        if amount > 0 and self._balance - amount >= 0:
            # can also be written with a conditional expression: if self.balance >= amount > 0:
            try:
                self._balance -= amount
                print(f"You have withdrawn £{amount}.")

            except InsufficientFunds as ex:
                print(f"You have insufficient funds.")
