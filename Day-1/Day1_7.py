#7) Using for loop, write and run a Python program to find factorial from 0 to 10.


def factorial(i,fact):
    for i in range(1, 11):
        fact = fact*i
        print(fact)
factorial(1,1)