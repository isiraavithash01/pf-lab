
animels=[]

for i in range(5):
    b=input("Enter the names :")
    animels.append(b)

print(animels[i])  
    
for i in range(5):
    print(animels[i])

    
print("------")

for index,value in enumerate(animels,start=1):
    print(index,value)



print("------")


count=0
for i in animels:
    if len(i)>5:
        count=count+1
print(count)        