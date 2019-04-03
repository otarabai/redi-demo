class bankaccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount

    def withdrawal(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('amont not available')
        return self.balance

p=bankaccount(1000)
#p.deposit(120)
p.withdrawal(2000)
#p.balance

print(p.balance)