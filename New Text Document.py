#Vote Eligible System

#inputs
age=int(input("Enter Your Age : "))
city=int(input(" Enter '1' if you'r sitizen if your not citixen press '2' : "))

#calulations

if age>18 :
    if city==1:
        print("Eligible to Vote!")
    else:
        print("Not Eligible To vote")

else: print("Not Eligible To vote")       
