def atm_service(option):
    current_balance = 1000
    if option == 1:
        deposit_amount = int(input("Enter the amount to deposit: "))
        current_balance += deposit_amount
        return f"Your updated account balance is {current_balance}."
    elif option == 2:
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        if withdraw_amount > current_balance:
            return "Insufficient funds in your account."
        else:
            current_balance -= withdraw_amount
            return f"Your updated account balance is {current_balance}."
    elif option == 3:
        return f"Your current account balance is {current_balance}."
    else:
        return "Thank you for using the ATM. Have a nice day!"

choice = int(input('''Please choose an option:
1. Deposit
2. Withdraw
3. Check Balance
0. Exit
Enter your choice: '''))
print(atm_service(choice))
