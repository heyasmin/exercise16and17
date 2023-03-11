from account import Account


class Savings(Account):
    def __init__(self, amount):
        super().__init__(self)
        self.balance = amount
