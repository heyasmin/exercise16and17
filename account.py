class Account:
    def __init__(self, initial_amount):  # this is the constructor, it creates the object
        self.balance = initial_amount

    def deposit(self, amount):  # deposit is a method!
        self.balance += amount
        print(f"You have deposited £{amount}.")

    def get_balance(self):  # getter
        return self.balance

    def withdraw(self, amount):
        try:
            if self.balance - amount >= 0:
                self.balance -= amount
                print(f"You have withdrawn £{amount}.")
        except InsufficientFunds as error:
            if self.balance - amount < 0:
                print(error)
        finally:
            print("You have insufficient funds.")



