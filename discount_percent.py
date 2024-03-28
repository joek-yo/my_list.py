def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price - (price * discount_percent / 100)
        return discount_price
    
    else:
        return price
    
#prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# print the final price
print(f"The final price after applying the discount is: {final_price}")