a=1
odd=0
even=0

while a<=5:
    num=int(input("Enter your Number :"))
    if num%2==0:
        even +=1
        num=num-num
        

    else:
        odd +=1
        num=num-num
    a=a+1    

print("Even Num tot :",even)
print("Odd Num tot :",odd)  

