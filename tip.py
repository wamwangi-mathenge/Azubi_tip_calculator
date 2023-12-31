# The program should ask the user to enter the charge for the food
charge = input("Charge for food = $")
print()

# Calculate the amounts of an 18% tip and 7% sales tax on the charge of the food
tip = float(charge) * 0.18
rounded_tip = round(tip, 2)
print(f"Tip = ${rounded_tip}")
print()
sales_tax = float(charge) * 0.07
rounded_sales = round(sales_tax, 2)
print(f"Sales tax = ${rounded_sales}")
print()
# Add everything together and display the charge of the food plus tip and sales tax
grand_total = float(charge) + float(rounded_tip) + float(rounded_sales)
print(f"Grand total = ${grand_total}")