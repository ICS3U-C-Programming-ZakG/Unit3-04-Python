#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 18, 2023
# This program tells the user whether their inputted number is positive, negative or zero.


def main():
    # Introduce program to user
    print(
        "This program gets the user input and tells them whether it's positive, negative or zero!\n"
    )

    # Get user number
    user_number = int(input("Please enter any number: "))

    # Check if user number is negative, positive or zero and display response
    if user_number >= 1:
        print("{} is a positive number.".format(user_number))
    elif user_number <= -1:
        print("{} is a negative number.".format(user_number))
    elif user_number == 0:
        print("{} is just zero!".format(user_number))
    else:
        print("No idea!")


if __name__ == "__main__":
    main()
