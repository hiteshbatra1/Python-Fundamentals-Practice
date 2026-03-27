#Q1 Create a BankAccount class with methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__ (self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    #METHOD TO DEPOSIT IN BANK ACCOUNT:
    def add_deposit (self, deposit_ammount):
        self.balance += deposit_ammount
        print(f"Total Balance Now: {self.balance}")

    #METHOD TO WITHDRAW FROM BANK ACCOUNT:
    def withdraw (self, withdraw_ammount):
        self.balance -= withdraw_ammount
        print(f"Total Balance Now: {self.balance}")

    #METHOD FOR CHECK BALANCE:
    def check_balance (self):
        print(f"The Current Balance Is RS.{self.balance}")

#INSTANCE OF BANKACCOUNT CLASS:
acc1 = BankAccount(12345, "Hitesh", 100000)

#DEPOSIT OF 100000:
acc1.add_deposit(100000)

#WITHDRAW OF 50000:
acc1.withdraw(50000)

#CHECK BALANCE:
acc1.check_balance()

print(acc1.account_number,acc1.owner_name,acc1.balance)
