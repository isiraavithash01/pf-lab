#Pharmacy Management System 

med_code=["MED001", "MED002", "MED003", "MED004", "MED005","MED006", "MED007", "MED008", "MED009", "MED010"]
med_name=["Paracetamol", "Vitamin C", "Cough Syrup", "Antacid","Pain Relief Gel", "Face Mask Pack", "Hand Sanitizer","Bandage Roll", "Antibiotic Cream", "Digital Thermometer"]
unit_price=[120.00, 450.00, 780.00, 350.00, 920.00,190.00, 520.00, 250.00, 680.00, 2150.00]

print("")   
print("-"*50)   
print(f"{'Medicine_Code':<20}{'Medicine_Name':<20}{'Price (Rs.)':<10}")
print("-"*50)
for i in range(len(med_code)):
  print(f"{med_code[i]:<20}{med_name[i]:<20}{unit_price[i]:<10.2f}") 
print("-"*50) 
print("") 

#calculations 
bill = []
final_bill = 0

while True:

    code = input("\nEnter Medicine Code : ").upper()

    if code in med_code:

        index = med_code.index(code)

        qty = int(input("Enter Quantity : "))

        total = qty * unit_price[index]
        final_bill = final_bill + total

        bill.append([med_code[index], med_name[index], qty, unit_price[index], total])

        print("Medicine Added Successfully!")

    else:
        print("Invalid Medicine Code!")

    choice = input("Do you want to add another medicine? (Y/N): ").upper()

    if choice != "Y":
        break

#Final Bill


print("")
print("="*80)
print(f"{'Code':<12}{'Medicine Name':<25}{'Qty':<8}{'Unit Price':<15}{'Total':<10}")
print("="*80)

for item in bill:
    print(f"{item[0]:<12}{item[1]:<25}{item[2]:<8}{item[3]:<15.2f}{item[4]:<10.2f}")

print("="*80)
print(f"{'Final Bill Amount :':<60}Rs. {final_bill:.2f}")
print("="*80)