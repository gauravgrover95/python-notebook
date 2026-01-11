"""
Dictionaries
"""

user_dict = {
    'username': 'gauravgrover',
    'name': 'Gaurav',
    'age': 32
}

user_dict['married'] = True
print(len(user_dict))
print()

# print(user_dict)
for k, v in user_dict.items():
    print(k, "=", v)
print()

user_dict2 = user_dict.copy()
print('user_dict', user_dict)
print('user_dict2', user_dict2)
print()

user_dict.pop('age')
print('user_dict', user_dict)
print('user_dict_2', user_dict2)

user_dict.clear()
print(user_dict)

del user_dict
