#4] Write a Python function to find the maximum of three numbers.

n1= int(input("Enter first number: "))
n2 = int(input("Enter second Number "))
n3 = int(input("Enter third Number: "))

if n1>n2>n3:
    print(f"{n1} is greatest")

elif n1<n2>n3:
    print(f"{n2} is greatest")

elif n1<n2<n3:
    print(f"{n3} is greatest")

else:
    print("All are equal")