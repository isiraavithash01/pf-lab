#University Course Fee Calculator 

print("University Semester Fee Calculator")

#Inputs

number_of_modules=int(input("Enter the number of modules: "))
fee_per_module=float(input("Enter the fee per module: "))
library_fee=float(input("Enter the library fee: "))
registration_fee=float(input("Enter the registration fee: "))

#Calculations

total=(number_of_modules*fee_per_module)+library_fee+registration_fee

#Output

print("\n---Payment Summary---")
print(f"Number of Modules: {number_of_modules:.2f}")
print(f"Fee per Module: Rs{fee_per_module:.2f}")
print(f"Library Fee: Rs{library_fee:.2f}")
print(f"Registration Fee: Rs{registration_fee:.2f}")
print(f"Total Fee: Rs{total:.2f}")
