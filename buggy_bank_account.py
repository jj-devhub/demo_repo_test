class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = balance
    
    def deposit(self, amount):
        # Bug fixed: validate positive amounts
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        # Bug fixed: check for sufficient balance and positive amount
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance
    
    def transfer(self, other_account, amount):
        # Bug fixed: validate amount and balance before transfer
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        if not isinstance(other_account, BankAccount):
            raise TypeError("Can only transfer to another BankAccount")
        
        self.balance -= amount
        other_account.balance += amount

# Test the buggy class
account1 = BankAccount(100)
account2 = BankAccount(50)

print(f"Account1 initial balance: ${account1.balance}")
print(f"Account2 initial balance: ${account2.balance}")

# These should fail but won't with buggy implementation
account1.deposit(-50)  # Negative deposit
print(f"After negative deposit: ${account1.balance}")

account1.withdraw(200)  # Overdraft
print(f"After overdraft: ${account1.balance}")

account1.transfer(account2, -100)  # Negative transfer
print(f"After negative transfer - Account1: ${account1.balance}, Account2: ${account2.balance}")
