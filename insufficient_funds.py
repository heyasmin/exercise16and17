# the Insufficient Funds Exception has to be in a different file, to be raised when needed

class InsufficientFunds(Exception):
    print(f"This would make you overdrawn.")

