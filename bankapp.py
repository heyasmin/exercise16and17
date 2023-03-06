from account import Account


class Current(Account):
    def __init__(self, amount):
        super().__init__(self)
        self.balance = amount


class Savings(Account):
    def __init__(self, amount):
        super().__init__(self)
        self.balance = amount


mirfat_current = Current(1000)
mirfat_savings = Savings(200)
print(f"Mirfat's current: £{mirfat_current.get_balance()}, Mirfat's savings: £{mirfat_savings.get_balance()}")

pam_current = Current(500)
pam_savings = Savings(100)
print(f"Pam's current: £{pam_current.get_balance()}, Pam's savings: £{pam_savings.get_balance()}")

eyasmin_current = Current(300)
eyasmin_savings = Savings(400)
print(f"Eyasmin's current: £{eyasmin_current.get_balance()}, Eyasmin's savings: £{eyasmin_savings.get_balance()}")

print(30 * "-")

pam_savings.deposit(150)

eyasmin_current.withdraw(500)


