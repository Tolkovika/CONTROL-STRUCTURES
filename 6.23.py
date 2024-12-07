number = int(input("Enter a number to create its multiplication table: "))
print(f"Multiplication table for {number}:")
for i in range(1, 10):  
    result = number * i
    print(f"{number} x {i} = {result}")