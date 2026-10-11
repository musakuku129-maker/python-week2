# Simple Bill Calculator

This project is a small Python program that asks the user for the price of one item and the quantity wanted, calculates the total, and prints a friendly summary using an f-string.

## How it works

1. Prompt the user for the item price.
2. Prompt the user for the quantity.
3. Convert the values from strings to numeric types.
4. Calculate the total.
5. Print the result in a neat format.

## Example

```python
price_per_item = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price_per_item * quantity

print(f"{quantity} items at {price_per_item:.2f} each = {total:.2f}")
```

## Example output

```text
Enter the price of one item: 50
Enter the quantity: 3
3 items at 50.00 each = 150.00
```

## Run it

```bash
python bill_calculator.py
```
