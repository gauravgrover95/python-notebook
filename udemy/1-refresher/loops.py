"""
For and While
"""

my_list = [1, 2, 3, 4, 5, 6, 7]

# for loop in list
for x in my_list:
    print(x)
print()

# for loop in range
for x in range(3, 6):
    print(x)
print()

# sum list
sum_loop = 0
for x in my_list:
    sum_loop += x
print(sum_loop)

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for x in my_list:
    print("Happy " + x)
print()

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 6:
        break
    print(i)

