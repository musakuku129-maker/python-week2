# Simple Bill Calculator

price_per_item = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price_per_item * quantity

print(f"{quantity} items at {price_per_item:.2f} each = {total:.2f}")
