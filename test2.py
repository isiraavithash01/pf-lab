print("Student GPA Calculator ")

x=int(input("Enter subjects 1 marks"))
y=int(input("Enter subjects 2 marks"))
z=int(input("Enter subjects 3 marks"))
c=int(input("Enter subjects 4 marks"))

tot=x+y+z+c
avg= tot/4
gpa=avg/25

print("Total marks = " , tot )
print("Avarage = " , avg )
print("GPA = " , gpa )
