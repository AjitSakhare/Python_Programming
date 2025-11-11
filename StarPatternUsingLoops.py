# *
# * *
# * * *
# * * * *
# * * * * *

#First Way
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

#Second way using repeat
for i in range(1,6):
        print("* " * i)

