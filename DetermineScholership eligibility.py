#Determine Scholership eligibility System

#input
mark=float(input("Enter Your Marks: "))

if mark>=75:
    inc=float(input("Enter Your Family Income : ")) 
    if  inc<=50000:
          print("Scholership Apporoved!")
    else:
       print("Scholership Deny!")     
else: 
    print("Not Enough Marks!")          