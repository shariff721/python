
class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    def deposit(self,amount):
        self.balance += amount
        return self


    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self



    def display_account_info(self):
        print(f" Interest Rate: {self.int_rate}\n Account Balance: {self.balance}")
        return self


    def yield_interest(self):
        self.balance += self.int_rate*self.balance
        return self
    
    @classmethod
    def print_all_instances(cls):
        for account in cls.all_accounts:
            print(account.balance)
            print(account.int_rate)

account_1 = BankAccount(0.21,500)
account_2 = BankAccount(0.25,200)


account_1.deposit(50).deposit(150).deposit(100).withdraw(175).yield_interest().display_account_info()
account_2.deposit(65).deposit(158).withdraw(50).withdraw(120).withdraw(30).withdraw(25).yield_interest().display_account_info()

BankAccount.print_all_instances()