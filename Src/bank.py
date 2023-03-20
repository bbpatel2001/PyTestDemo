class InSufficientBalance(Exception):
    pass


class Bank(object):
    def __init__(self, name="", amount=0):
        self.balance = amount
        self.name = name.title()
    
    def deposit(self,amount):
        if amount < 1:
            amount = 0
        self.balance += amount

    def withdraw(self,amount):
        if self.balance < amount:
            raise InSufficientBalance
        self.balance -= amount
    
    def set_account_holder_name(self, name):
        if not isinstance(name,str):
            TypeError("Name should be in string formate")
        self.name = name.title()
        
    def get_balance(self) ->  int :
        return (self.balance)
    
    def get_account_holder_name(self) -> str :
        return(self.name)
