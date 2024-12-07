# Program that calculates the amount to be paid
#
number_of_products = int(input("Enter the number of purchased products: "))
price = float(input("Enter a product price: "))
total_amount = number_of_products * price

if number_of_products > 2:
    total_amount *= 0.75  
    print(f"Amount to be paid is {total_amount: }")
else:
    print(f"A discount is unavailable. Total amount is {total_amount: }")


 