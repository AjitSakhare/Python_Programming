#Calculate factorial of number

def factorial(number):
    if number==1:
        return number
    else:
         factorial_result = number * factorial((number-1))
         return factorial_result

num=int(input("Enter number to calculate factorial:"))

result=factorial(num)

print(f"Factorial of {num} is: {result}")



