""" This program aims at requesting a user input as integers that will be
    stored and an average value calculated at the end when the user inputs
     a value of -1"""

# create a total value starting from 0 that will sum up all values inputted
# create a counter value that will count the number of inputs
total = 0
counter = 0
user_input = int(input("Please enter a number of your choice: "))

""" as long as user inputs an integer that is not -1, the value will be added
to the total and the counter will increase by 1 with each input"""
while user_input != -1:
    total += user_input
    counter += 1
    user_input = int(input("Please enter another number or type -1 to exit: "))

# calculate and print average of all user inputs excluding -1 exit prompt
    if user_input == -1:
        print((total)/(counter))
        break
