# Simple Bill Calculator

This project is a small Python program that asks the user for a product name, the price of one item, and the quantity wanted. It then calculates the total and prints a friendly summary using an f-string.

## How it works

1. Prompt the user for the product name.
2. Prompt the user for the item price.
3. Prompt the user for the quantity.
4. Convert the values from strings to numeric types.
5. Calculate the total.
6. Print the result in a neat format.

## Example

```python
product_name = input("Enter the product name: ")
price_per_item = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price_per_item * quantity

print(f"{quantity} {product_name}s at {price_per_item:.2f} each = {total:.2f}")
```

## Example output

```text
Enter the product name: apple
Enter the price of one item: 50
Enter the quantity: 3
3 apples at 50.00 each = 150.00
```

## Run it

```bash
python bill_calculator.py
```
