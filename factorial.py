
#This is a simple program to calculate factorial of a program
a=eval(input())
def factorial(number):
    if number <=1:
        return 1
    else:
        return number*factorial(number-1)
print(factorial(a))

