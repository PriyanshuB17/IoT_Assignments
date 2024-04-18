#6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

fact = 1
def factorial(n1):
    for i in range (1, n1+1):
        global fact  
        fact = fact * i
    print(f"Factorial of {n1} is {fact}")

factorial(7)
