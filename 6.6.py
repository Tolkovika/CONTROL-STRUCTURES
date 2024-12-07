# Parking meter fee calculator
hours = int(input("Enter number of hours parked: "))

if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
else:
    fee = 20

print(f"Parking fee: {fee} PLN")
