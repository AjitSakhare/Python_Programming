#In this we write a python code to count sum of all number from 1 to 50

total_sum=0
for i in range(1,50+1):  # here is confusion for me it's ok to give like this?
    total_sum+=i

print(f"The sum of numbers from 1 to 50 is:", total_sum)