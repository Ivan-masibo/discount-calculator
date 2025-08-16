#question 1. calculate _discount (price, discount_percentage)


def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = (price * discount_percent) / 100
        final_price = price - discount_price
        return final_price
    else:
        # If the discount percentage is less than 20, return the price
        return price
price = float(input("Enter the price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percentage)
print("The final price after discount is Sh:", final_price)

