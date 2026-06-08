#Atm Cash Withdrawal System
blance=float(20000)
#inputs
pin=int(input("enter your pin: "))

#Calculations
if pin==1234:
    a=float(input("Enter Your Amount: "))

    if   a<=blance:
        print("Withdrawla Successfull!")
    else: 
        print("Not Enoughf Blance!")    
else:
    print("Worrng Pin number!")    