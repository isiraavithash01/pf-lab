#Electricity Bill Calculater

#inputs 
tc=0
for i in range(1,6):
    uni=int(input("Enter unit for coustomer {i}:"))
    if uni<=100:
        bill=uni*10
    elif uni <=200:
        bill=(100*10)+((uni - 100)*15)
    else: bill=(100*10)+(100*15)+((uni-200)*20)
print("bill Amount=rs.",bill)
tot=bill 
print("Total Amount Collect= rs.",tot)
