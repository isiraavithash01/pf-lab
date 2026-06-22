
e=0
n=0
for i in range(1,11):
    uni=int(input("Enter the attendence {i}:"))
    if uni>=75:
        print("Eligible")
        e=e+1
    else:
         print("Not Eligible!") 
         n=n+1
           
avg=e/10
print("Avrage",avg)
print("Eligible Count",e)
print("Not Eligible Count",e)