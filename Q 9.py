# Cinema Ticket Booking System 

print("---Cinema Ticket Booking System---")

#Inputs

adult_tickets_price=float(input("Enter the price of an adult ticket: "))
adult_tickets_quantity=int(input("Enter the number of adult tickets: "))
child_tickets_price=float(input("Enter the price of a child ticket: "))
child_tickets_quantity=int(input("Enter the number of child tickets: "))
snack_package_cost=float(input("Enter the cost of the snack package: "))

#calculations

adult_total=adult_tickets_price*adult_tickets_quantity
child_total=child_tickets_price*child_tickets_quantity
total=adult_total+child_total+snack_package_cost

#Output

print("\n---Invoice---")

print(f"Adult Tickets: {adult_tickets_quantity} x Rs{adult_tickets_price:.2f} = Rs{adult_total:.2f}")
print(f"Child Tickets: {child_tickets_quantity} x Rs{child_tickets_price:.2f} = Rs{child_total:.2f}")
print(f"Snack Package: Rs{snack_package_cost:.2f}")
print(f"Total Bill: Rs{total:.2f}")