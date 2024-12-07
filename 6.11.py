# Product price reduction checker
current_price = float(input("Enter current product price: "))
previous_price = float(input("Enter previous product price: "))

reduction_percentage = ((previous_price - current_price) / previous_price) * 100

if reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction_percentage:.0f}%")
else:
    print("No significant discount.")
