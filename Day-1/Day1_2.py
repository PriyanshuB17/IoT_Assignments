# 2] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values 
    # If user enters a 4 digit number 9361 output should be
    # a. 9 3 6 1
    # b. 9361 = 9 000 + 300 + 60 + 9
    # c. 1639

num = int(input("Enter the four digit number: "))

temp = num
rev = 0
while(temp != 0):
    rem = int(temp % 10)
    rev = int(rev * 10 + rem)
    temp = int(temp / 10)
    
pmet = rev #1369

print("a. ", end=" ")
while(pmet != 0):
    rem=int(pmet%10)
    pmet=int(pmet/10)
    print(rem, end=" ")
print()

pmet = rev

sum = 0
cnt = 1000
print("b. ", end=" ")
while(pmet != 0):
    rem = pmet % 10
    sum = rem * cnt
    cnt = int(cnt / 10)
    pmet = int(pmet / 10)
    print(f"{sum} +", end=" ")
print()

print(f"c.  {rev}", end=" ")
print()
