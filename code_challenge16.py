def denomination(amount):
    isa_l = amount // 1000
    isa_s = amount % 1000
    
    five_h = isa_s // 500
    five_s = isa_s % 500
    
    two_h = five_s // 200
    two_s = five_s % 200
    
    one_h = two_s // 100
    one_s = two_s % 100
    
    fifty = one_s // 50
    f_s = one_s % 50
    
    bente = f_s // 20
    b_s = f_s // 20
    
    ten = b_s // 10
    t_s = b_s % 10
    
    one = t_s // 1
    print(f"The account balance is {account_balance} and breakdown into PH denomination:")
    print(f" {isa_l} -- 1000")
    print(f" {five_h} -- 500")
    print(f" {two_h} -- 200")
    print(f" {one_h} -- 100")
    print(f" {fifty} -- 50")
    print(f" {bente} -- 20")
    print(f" {ten} -- 10")
    print(f" {one} -- 1")
    
print("Welcome to the Banking System!")

account_name = ""
account_balance = 0
program_running = True

while program_running:
    print("\nChoose an option: \n1 - Create Account \n2 - Deposit Money \n3 - Withdraw Money \n4 - Check Balance \n5 - Exit Program")
    option = input("Enter your choice (1-5): ")

    if option == "1":
        account_name = input("Enter your name: ")
        account_balance = float(input("Enter initial deposit: "))
        print("Account created for", account_name, "with balance of", account_balance, "PHP.")
    
    elif option == "2":
        if account_name == "":
            print("No account found. Please create an account first.")
        else:
            deposit_amount = int(input("Enter the amount to deposit: "))
            account_balance += deposit_amount
            print("You deposited", deposit_amount, "PHP. Current balance is", account_balance, "PHP.")

    elif option == "3":
        if account_name == "":
            print("No account found. Please create an account first.")
        else:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if withdraw_amount > account_balance:
                print("Insufficient balance!")
            else:
                account_balance = account_balance - withdraw_amount
                print("You withdrew", withdraw_amount, "PHP. Current balance is", account_balance, "PHP.")

    elif option == "4":
        if account_name == "":
            print("No account found. Please create an account first.")
        else:
            print("Account Name:", account_name)
            print("Current Balance:", account_balance, "PHP")
            print("Denomination Breakdown:")
            amount = account_balance
            denomination(amount)

    elif option == "5":
        print("Exiting the program. Goodbye!")
        program_running = False

    else:
        print("Invalid choice. Please try again.")
