from account import Account


class Current(Account):
    def __init__(self, amount):
        super().__init__(self)
        self._balance = amount


class Savings(Account):
    def __init__(self, amount):
        super().__init__(self)
        self._balance = amount


mirfat_current = Current(1000)
mirfat_savings = Savings(200)

pam_current = Current(500)
pam_savings = Savings(100)

eyasmin_current = Current(300)
eyasmin_savings = Savings(400)

print(f"Mirfat's current account's starting balance is £{mirfat_current.get_balance()}.")

pam_savings.deposit(150)
# how to add the deposit amount in the print statement?
print(f"Pam's savings balance is now £{pam_savings.get_balance()}.")

eyasmin_current.withdraw(-100)
print(f"Eyasmin's current account's balance is £{eyasmin_current.get_balance()}.")