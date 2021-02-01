print("Enter the number to check whether it is fizzbuzz number or not")

fizzbuzz_number = int(input())

def fizz_buzz():
    if(fizzbuzz_number % 3 == 0):
        print("Fizz")
    elif(fizzbuzz_number % 5 == 0):
        print("Buzz")
    elif(fizzbuzz_number % 3 == 0 and fizzbuzz_number % 3 == 0):
        print("FizzBuzz")
    else:
        print(fizzbuzz_number)

fizz_buzz()