class User(object):
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} attacking with the power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows =arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

class Hybrid(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)



hb1 = Hybrid('Tony', 499, 678)

print(hb1.attack())
print(hb1.check_arrows())
print(hb1.sign_in())