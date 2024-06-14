def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompting the user to enter inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print(f"No discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"Discount applied. Final price after discount: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
