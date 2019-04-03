'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def next_birthday(self):
        self.age += 1

    def say_hi(self):
        print('Hello, my name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old.')

    def is_adult(self, restriction=18):
        return self.age >= restriction

p = Person('Mohammadreza', 35)
p.say_hi()
p.next_birthday()
print(p.age)
#print(type(p))
if p.is_adult():
    print(f'{p.name} is an adult' )
else:
    print(f'{p.name} is a child')
'''

"""
class BankAccout:
    def __init__(self, balance = 0, currency = 'Euro'):
        self.balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.balance += amount


    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(" you don't have enough money")
        return self.balance

    def currency_exchange(self, unit):

        if unit == self.currency:
            print(f'{self.balance} + {self.currency}')
        elif unit == '$':
            exchange= self.balance*1.13
            print(f'you have {exchange} $')
        elif unit == 'Pound':
            exchange= self.balance*0.85
            print(f'you have {exchange} Pounds')


'''
p = BankAccout()
p.deposit(350)
print(p.balance)

p.withdrawal(50)
print(p.balance)
p.withdrawal(400)

p.currency_exchange('Pound')
'''


class Turtle:
    def __init__(self, x, y, ):
        self.x = x
        self.y = y

    def move_left(self, steps):
        final_position = self.x - steps
        if final_position < 0:
            final_position = 0
        self.x = final_position

    def move_right(self, steps):
        final_position = self.x + steps
        if final_position > 10:
            final_position = 10
        self.x = final_position

    def move_up(self, steps):
        final_position = self.y + steps
        if final_position > 10:
            final_position = 10
        self.y = final_position

    def move_down(self, steps):
        final_position = self.y - self
        if final_position < 0:
            final_position = 0
        self.y = final_position

    def get_position(self):
        return self.x, self.y


myturtle = Turtle(3, 3)
myturtle.move_left(5)
myturtle.move_up(5)
print(myturtle.get_position())

"""





class Todo_list:
    def __init__(self, items=['todo']):
        self.items = items
    def add_item(self, description):
        x = description
        (self.items).append('x')

    def mark_item_as_done(self, item_number):
        done_list = []





