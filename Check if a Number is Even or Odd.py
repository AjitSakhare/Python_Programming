#In this program we are going to take input from user and check weather numer is odd or even.

input_number = int(input("Enter a number:"))

if input_number % 2 == 0:  # checks if number divided by 2 completely then its even otherwise it's odd.
    print(f"{input_number} is an even number.")
else:
    print(f"{input_number} is an odd number.")