'''
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
'''

animals = ["dog", "cat", "elephant", "lion", "monkey"]
print(animals)

# remove animal at 3rd index
animals.remove(animals[2])
print(animals)

## -> Correction, assignment asked to remove 3rd index not the third element
## -> Improvment: we could use list.pop(), it directly remove the element at a particular position

# append
animals.append("cheetah")
print(animals)

# delete 0
animals.remove(animals[0])
print(animals)

# print
print(animals)

# print first 3
print(animals[0:3])
