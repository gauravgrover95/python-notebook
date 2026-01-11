from animal import Animal

class Dog(Animal):

    can_shed: bool
    domestic_name: str

    def __init__(self, name):
        super().__init__()
        self.domestic_name = name

    def eat(self):
        print('Chew on bones!')

    def talk(self):
        print('Bark!')
