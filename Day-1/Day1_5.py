# 5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

avg = (sub1+sub2+sub3)/3

print(f"Average of marks: {avg}")

if(90<=avg<=100):
    print(f"Grade: A")

elif (80<=avg<=89):
    print(f"Grade: B")

elif (70<=avg<=79):
    print(f"Grade: C")

elif(60<=avg<=69):
    print(f"Grade: D")

elif(0<=avg<=59):
    print(f"Grade: F")

else:
    print("Invalid Input!!")