# The program should ask the user to enter the charge for the food
charge = input("Charge for food = $")
print()

# Calculate the amounts of an 18% tip and 7% sales tax on the charge of the food
tip = float(charge) * 0.18
rounded_tip = round(tip, 2)
print("Tip =", rounded_tip)

sales_tax = float(charge) * 0.07
rounded_sales = round(sales_tax, 2)
print("Sales tax =", rounded_sales)