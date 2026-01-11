"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""

def get_person(firstname, lastname, age):
    return {
        'firstname': firstname,
        'lastname': lastname,
        'age': age
    }

gaurav = get_person('Gaurav', 'Grover', 30)
print(gaurav)
print()