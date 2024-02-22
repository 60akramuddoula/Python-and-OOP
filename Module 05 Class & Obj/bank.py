class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 5000
        self.max_withdraw = 20000

    def get_balance(self): 
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.max_withdraw:
            print(f'Sorry, you cannot withdraw above {self.max_withdraw}')
        elif amount < self.min_withdraw:
            print(f'Sorry, withdrawal amount must be at least {self.min_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money: {amount}')
            print(f'Balance after withdrawal: ${self.get_balance()}')
    
    def deposit(self, amount):
        self.balance += amount
        print('Deposited successfully')
        print(f'After deposit, current balance is {self.get_balance()}')


dbbl = Bank(50000)

dbbl.deposit(5000)
dbbl.withdraw(8000000)
dbbl.withdraw(5000)
