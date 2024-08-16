class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self.__balance}.")

    def check_balance(self):
        return self.__balance

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account_number, initial_balance=0):
        account = Account(account_number, initial_balance)
        self.accounts.append(account)
        print(f"Account {account_number} created for {self.name}.")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

# Example usage
customer = Customer("John Doe")
customer.create_account(12345, 100)
customer.create_account(67890, 200)

account = customer.get_account(12345)
account.deposit(50)
account.withdraw(30)
print("Balance:", account.check_balance())
