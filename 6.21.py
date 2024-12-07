# Program to break down an amount into 1 PLN, 2 PLN, and 5 PLN coins
amount = int(input("Enter the amount in PLN: "))

five_pln_coins = amount // 5  
amount = amount % 5           

two_pln_coins = amount // 2   
amount = amount % 2           

one_pln_coins = amount        

print("The amount in coins:")
print("5 PLN coins:", five_pln_coins)
print("2 PLN coins:", two_pln_coins)
print("1 PLN coins:", one_pln_coins)