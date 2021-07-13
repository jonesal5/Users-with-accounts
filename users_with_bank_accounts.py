Class User:

def __init__(self, name, email, int_rate, balance):
    self.name = name
    self.email = email
    self.account = BankAccount(int_rate=0.00, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amoount)
        return self`

    def display_user_balance(self):
        print("User: {self.name}, Email: {self.email}")
        self.account.display_account_info()
        return self

    user1= User('Alyssa', 'alyssak@gmail.com')
    Alyssa.make_deposit(100)..make_deposit(300).make_withdrawal(350).display_user_balance()

    user2= User('Taytum', 'Taytumr@gmail.com', '1,000')
    Taytum.make_withdrawal(100).make_withdrawal(200)
    
    user2.display_user_balance()
    user2.account_yield_interest()
    user2.display_user_balance()

Class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = init_rate
        self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            return self
        
        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else: 
                self.balance -= 5
                print("Insufficient Funds: Charging a $5 fee")
            return self

        def display_account_info(self):
            print("Balance: $(self.balance")
            return self
        
        def yield_interest(self):
            if self.balance > 0:
                self.balance = self.balance + self.balance * self.int_rate
            return self

# update the User class __init__ method

# update the User class make_deposit method

# update the User class make_withdrawal method

# update the User class display_user_balance method

# BONUS allow a user to have multiple accounts; update methods so the user has to specify which account they are depositing to or withdrawing from.
