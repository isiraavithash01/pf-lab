#Mobile Data Usage Calculator

print("---Calculate Your Internet Bill---")

#Inputs

data_usage=float(input("Enter your data usage in GB: "))
cost_per_GB=float(input("Enter the cost per GB: "))
service_charges=float(input("Enter the service charges: "))

#Calculations

datacost=data_usage*cost_per_GB
tot=datacost+service_charges

#Output

print("\n---Internet Bill---")\

print(f"Data Cost: {datacost:.2f} GB")
print(f"Additional charges: Rs{service_charges:.2f}")
print(f"Total Bill: Rs{tot:.2f}")
