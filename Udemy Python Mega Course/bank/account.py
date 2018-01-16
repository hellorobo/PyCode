class Account:

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("+%d" % amount)

    def withdrawal(self,amount):
        self.balance = self.balance - amount
        print("-%d" % amount)

    def commit(self, filepath):
        with open(filepath, 'w') as file:
            file.write(str(self.balance))

    def total(self):
        return self.balance


filepath = r'balance.txt'
account = Account(filepath)

print("current balance is %d" % account.total())
account.deposit(150)
print("current balance is %d" % account.total())
account.withdrawal(75)
print("current balance is %d" % account.total())
account.commit(filepath)
