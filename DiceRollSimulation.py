#simple way
# import random
# print(random.choice(range(1,6)))

#Proper with input and formating
import random

print("Welcome to game of rolling dice.")

while True:
    choice=input("Press enter to roll a dice ")
    choice=choice.strip()
    if choice=='q':
        print("Thank you for playing a game. Bye!")
        break
    elif choice=='':
        number=random.randint(1,6)
        print(f"Your number is {number}")
    else:

        print("Invalid Number!!")
