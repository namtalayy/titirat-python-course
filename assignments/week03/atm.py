# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
# Complete the menu logic here
# Your code here:
        if choice == "1":
            print(f"Your balance is: ${balance}") 
            
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount 
                print(f"Withdraw: ${amount} balance now: ${balance}")
            else:
                print("Not enough balance!")
                
        elif choice == "3":
            amount = float(input("Enter amount to deposit: ")) 
            if amount > 0:
                balance += amount
                print(f"Deposit: ${amount} balance now: ${balance}")
            else:
                print("Invalid deposit amount!")
        elif choice == "4":
            print("Exiting...") 
            break
else:
    print("Invalid PIN") 