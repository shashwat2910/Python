import math

def bigger():
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    num3 = int(input("Enter third number "))

    bigger = max(num1, num2, num3)

    print("Bigger number is "+ repr(bigger))

bigger()