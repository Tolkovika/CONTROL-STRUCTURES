# Program to print numbers from 1 to 30 with special rules for divisibility

for number in range(1, 31):  # Loop through numbers 1 to 30
    if number % 3 == 0 and number % 5 == 0:  
        print("BINGO", end=" ")
    elif number % 3 == 0:  
        print("THREE", end=" ")
    elif number % 5 == 0:  
        print("FIVE", end=" ")
    else:  # Not divisible by 3 or 5
        print(number, end=" ")
