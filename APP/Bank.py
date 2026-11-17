balance = 10000
while True:
    print("\n----- BANK MENU -----")
    print("1. Check Balance 2. Deposit 3. Withdraw 4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Current Balance =", balance)
        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
            balance += amount
            print("Deposit successful.")
            print("Updated Balance =", balance)
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if amount > balance:
                raise ValueError("Insufficient balance.")
            balance -= amount
            print("Withdrawal successful.")
            print("Updated Balance =", balance)
        elif choice == 4:
            print("Thank you for using the bank application.")
            break
        else:
            raise ValueError("Invalid menu choice.")
    except ValueError as error:
        print("Error:", error)