from account import Account

mirfat_account = Account(1000)
pam_account = Account(500)
eyasmin_account = Account(300)
print(f"Mirfat's starting balance is £{mirfat_account.get_balance()}.")

pam_account.deposit(150)
# how to add the deposit amount in the print statement?
print(f"Pam has completed a deposit, the balance is now £{pam_account.get_balance()}.")