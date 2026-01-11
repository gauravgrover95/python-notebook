"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements, use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

REPEAT = 1
i = 0
while i < REPEAT:
    for ele in range(len(my_list)): # it is feasible and better to use `for ele in my_list`
        if my_list[ele] == "Monday":
            continue
        print(my_list[ele])
    i += 1
    print()


REPEAT = 3
i = 0
while i < REPEAT:
    for ele in range(len(my_list)): # it is feasible and better to use `for ele in my_list`
        if my_list[ele] == "Monday":
            continue
        print(my_list[ele])
    i += 1
    print()



