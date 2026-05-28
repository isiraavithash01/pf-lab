print("Employee Payroll System ")
x=float(input("Enter  basic salary"))
y=int(input("Enter  overtime hours"))
z=float(input("Enter overtime rate"))
c=float(input("Enter bonus"))
v=float(input("tax percentage"))



gtot=x+(y*z)+c
tx=gtot*20/100
tot=gtot-tx

print(" gross salary = RS.", gtot)
print(" tax amount = RS." , tx )
print(" net salary = RS." , tot )
