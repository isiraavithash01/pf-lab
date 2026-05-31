#Gym Membership Payment System 

#Inputs

monthly_fee=float(input("Enter the monthly fee: "))
number_of_months=int(input("Enter the number of months: "))
registration_fee=float(input("Enter the registration fee: "))
personal_trainer_fee=float(input("Enter the personal trainer fee: "))



#Calculations

total=(monthly_fee*number_of_months)+registration_fee+personal_trainer_fee

tax=total*5/100

final_payment=total+tax


#Output

print("--- Gym Membership Invoice ---")

print(f"Total: $",total)

print(f"Tax : $",tax)
print(f"Final payment: $",final_payment)
print(f"Thank you!")