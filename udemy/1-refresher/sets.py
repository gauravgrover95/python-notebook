my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print("length of set: ", len(my_set))


for x in my_set:
    print(x)

my_set.discard(3)
print(my_set)

my_set.clear()
print(my_set)

my_set.add(6)
print(my_set)

my_set.update([7, 8])
print(my_set)

# indexing :: ERROR
print(my_set[0])

