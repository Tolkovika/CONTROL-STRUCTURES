# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

def check_pin():
    """Verifies the user PIN."""
    entered_pin = input("Enter your PIN: ")
    return entered_pin == pin

def change_pin():
    """Allows the user to change their PIN after verification."""
    global pin
    if check_pin():
        new_pin = input("Enter a new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            confirm_pin = input("Confirm the new PIN: ")
            if new_pin == confirm_pin:
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("PIN confirmation does not match.")
        else:
            print("Invalid PIN. It must be exactly 4 digits.")
    else:
        print("Incorrect current PIN. Cannot change PIN.")

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if not check_pin():
        print("Incorrect PIN. Access denied.")
        continue

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        change_pin()
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  
    else:
        print("Invalid option. Please try again.")

