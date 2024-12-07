i = 6

while i >= 0:
    j = 1  # Start 'j' at 1, as in the original 'for' loop range(1, 4)
    
    while j <= 3:
        print(f'{i + j}', end=' ')  # Print the sum of 'i' and 'j'
        j += 1  # Increment 'j' to move to the next number
        
    print()  
    i -= 3  