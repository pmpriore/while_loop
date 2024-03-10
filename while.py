# ask user to input any number repeatedly until they wish to exit by typing -1
# calculate the average of all numbers the user has inputted excluding -1
# create a total value starting from 0 that will sum up all values inputted
# create a counter value that will count the number of inputs
# calculate and print average of all user inputs excluding -1 exit prompt

total = 0
counter = 0
user_input = int(input("Please enter a number of your choice: "))

while user_input != -1:
    total += user_input
    counter += 1
    user_input = int(input("Please enter another number or type -1 to exit: "))

    if user_input == -1:
        print((total)/(counter))
        break