class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def addingnum( cls, num1 , num2):
        return num1 + num2

player1 = PlayerCharacter('Cindy', 23)
player2 = PlayerCharacter('Tony', 25)

print(player1.name)
print(player1.age)
print(player2.shout())
print(player2.age)

player3 = PlayerCharacter.addingnum(4,5)

print(player3)