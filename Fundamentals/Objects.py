class Account:
    def __init__(self, account_number, account_type,initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        # Check if the deposit amount is valid
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        # Check if the withdrawal amount is valid
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

my_account = Account("123456789", "Savings", 1000)
my_account.account_number
my_account.account_type
my_account.balance

my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(1500)