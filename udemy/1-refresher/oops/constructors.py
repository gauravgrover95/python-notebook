"""
constructors
- default / empty constructor = created if no explicit constructor is passed
- no args constructor
- parameter constructor
"""

class Person:
    first_name: str
    last_name: str

    # default / empty
    def __init__(self):
        print('Default constructor being called')
        pass

    def __init__(self):
        print('No args constructor being called')
        print('New person created with no base values')

    def __init__(self, first_name: str, last_name: str):
        print('Parameter constructor being called')
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print(f'Hello my name is {self.first_name} {self.last_name}')

gaurav = Person(first_name='Gaurav', last_name='Grover')
gaurav.talk()