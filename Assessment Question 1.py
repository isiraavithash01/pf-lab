#Pharmacy Management System 

med_code=[]
med_name=[]
unit_price=[]
x=0
while x<3:
    a=str(input("Enter medicine Code :"))
    med_code.append(a)
    b=str(input("Enter medicin Name :"))
    med_name.append(b)
    c=float(input("Enter the unit price :"))
    unit_price.append(c)
    x=x+1
print("")   
print("-"*50)   
print(f"{'Medicine_Code':<20}{'Medicine_Name':<20}{'Price (Rs.)':<10}")
print("-"*50)
for i in range(len(med_code)):
  print(f"{med_code[i]:<20}{med_name[i]:<20}{unit_price[i]:<10.2f}") 