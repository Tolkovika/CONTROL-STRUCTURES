pin_0805 = 805
attempts = 3

while attempts > 0:
    pin = int(input("Enter the PIN code: "))
    
    if pin == pin_0805:
        print("PIN is accepted!")
        break  
    else:
        print("Incorrect...")
        attempts -= 1  
        
        if attempts == 0:
            print("Sorry, your payment card has been blocked.")

