def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Printing the final price
if final_price != original_price:
    print("Final price after applying discount: Ksh", final_price)
else:
    print("No discount applied. Original price: Ksh", original_price)
