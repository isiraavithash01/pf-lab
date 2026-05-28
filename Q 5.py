# Program to calculate the total bill for an online store

# Input prices and quantities of 3 products
product1_price = float(input("Enter the price of product 1: "))
product1_quantity = int(input("Enter the quantity of product 1: "))

product2_price = float(input("Enter the price of product 2: "))
product2_quantity = int(input("Enter the quantity of product 2: "))

product3_price = float(input("Enter the price of product 3: "))
product3_quantity = int(input("Enter the quantity of product 3: "))

# Input delivery charge and discount percentage
delivery_charge = float(input("Enter the delivery charge: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate total price for each product
product1_total = product1_price * product1_quantity
product2_total = product2_price * product2_quantity
product3_total = product3_price * product3_quantity

# Calculate subtotal
subtotal = product1_total + product2_total + product3_total

# Calculate discount amount
discount_amount = (discount_percentage / 100) * subtotal

# Calculate final total
total = subtotal - discount_amount + delivery_charge

# Display formatted invoice
print("\n--- Invoice ---")
print(f"Product 1: {product1_quantity} x ${product1_price:.2f} = ${product1_total:.2f}")
print(f"Product 2: {product2_quantity} x ${product2_price:.2f} = ${product2_total:.2f}")
print(f"Product 3: {product3_quantity} x ${product3_price:.2f} = ${product3_total:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount ({discount_percentage}%): -${discount_amount:.2f}")
print(f"Delivery Charge: +${delivery_charge:.2f}")
print(f"Total: ${total:.2f}")




#save 







