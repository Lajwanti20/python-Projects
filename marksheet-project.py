#Mini Project : Create a student marksheet with using loop.

#take input a marks from user
name = input("Enter a student name : ")

#take input a marks from user
marks1 = float(input("Enter English marks:"))
marks2 = float(input("Enter Python marks: "))
marks3 = float(input("Enter Maths marks:"))
marks4 = float(input("Enter Computer marks:"))
marks5 = float(input("Enter Physics marks:"))

#total marks
totalMarks = 500
print("Total marks is:", totalMarks)
#obtain marks
obtainMarks = marks1+marks2+marks3+marks4+marks5
print("Obtain marks is:", obtainMarks)
#percentage
percentage = (obtainMarks/totalMarks)*100
print("Percentage marks is:", percentage)

if percentage >= 80:
    print("Grade: A+\n Reslut : Pass")
elif percentage >= 70:
    print("Grade: A\n Reslut : Pass")
elif percentage >= 60:
    print("Grade: B\n Reslut : Pass")
elif percentage >= 50:
    print("Grade: C\n Reslut : You have passed but you need to improve your grade.")
elif percentage >= 40:
    print("Grade: D\n Reslut : You have passed but you need to improve your grade.")
else:
    print("Grade: Fail")


