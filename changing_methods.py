class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f'User:{self.name}, Balance: ${self.account_balance}')
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self

tommy = User('Tommy', 'tommy@tommy.com')
chuckie = User('Chuckie', 'chuckie@chuckie.com')
angelica = User('Angelica', 'angelica@angelica.com')

tommy.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(150).display_user_balance()

chuckie.make_deposit(500).make_deposit(200).make_withdrawal(50).make_withdrawal(100).display_user_balance()


angelica.make_deposit(1000).make_withdrawal(25).make_withdrawal(25).make_withdrawal(50).display_user_balance()

tommy.transfer_money(chuckie, 100).display_user_balance()
chuckie.display_user_balance()
