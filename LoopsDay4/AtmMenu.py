# Simple ATM Simulator with break: Create a simple loop that shows an "ATM" menu with options like "Deposit," "Withdraw,"
# and "Exit." Use break to end the program when the user chooses "Exit."

balance = 1000  # Starting bank balance

while True:
    # 1. Display the ATM menu
    print("\n--- ATM MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    # 2. Handle options using if-elif-else
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposited ${amount:.2f}. New Balance: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ${amount:.2f}. New Balance: ${balance:.2f}")
        else:
            print("Insufficient funds! Transaction canceled.")

    elif choice == "3":
        print("Thank you for using the ATM. Goodbye!")
        break  # Exits the loop and ends the program completely

    else:
        print("Invalid choice. Please select 1, 2, or 3.")