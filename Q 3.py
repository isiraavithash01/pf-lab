print("Vehicle Trip Cost Estimator  ")

x=int(input("Enter distance traveled"))
y=int(input("Enter fuel efficiency"))
z=int(input("Enter fuel price per liter"))
c=int(input("Enter highway charges"))

fu=x/y
fc=fu*z
tot=fu+fc+c



print("fuel used= ", fu)
print("fuel cost= " , fc )
print("final trip cost = " , tot )

