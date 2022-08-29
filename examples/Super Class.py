class User(object):
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
        print(f'attacking with the power of {self.power}')

player1 = Wizard('Cindy', 23, 'tony@gmail.com')
player2 = Wizard('Tony', 25, 'sdkgfkdsj@gmail.com')
player3 = User('tony@gmail.com')

print(player1.name)
print(player1.email)
print(player1.attack())
print(player3.sign_in())

