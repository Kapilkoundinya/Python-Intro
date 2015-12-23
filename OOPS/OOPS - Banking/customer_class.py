class Customer:

    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def with_draw(self, amount):
        if amount > self.balance:
            raise RuntimeError('Requested amount cannot be withdrawn!! out of balance')
        else:
            self.balance -= amount
            return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
