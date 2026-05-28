print("Hotel Billing System ")
x=float(input("Enter  room charge per day"))
y=int(input("Enter   number of days"))
z=float(input("Enter  food charges"))
c=float(input("Enter  service charge percentage"))

stot=x*y+z
sc=stot*c/100
tot=stot+sc


print("sub total=", stot)
print("service charge=" , sc )
print("final bill =" , tot )
