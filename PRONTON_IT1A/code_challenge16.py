
balance = 0 

def account(name, initial_deposit = 0):
    account_name = name
    b = 0
    b += initial_deposit
    b = balance
    print(f"Account created for {account_name} with inittial deposit of {balance}")

def ph_denomination(amount):
    isa_k = amount // 1000
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
    b_s = f_s % 20
    
    ten = b_s // 10
    t_s = b_s % 10

    one = t_s // 1 

    print("The account balance was breakdown into PH Denomination: ")
    print(f"{isa_k} = 1000")
    print(f"{five_h} = 500")
    print(f"{two_h} = 200")
    print(f"{one_h} = 1000")
    print(f"{fifty} = 1000")
    print(f"{bente} = 1000")
    print(f"{ten} = 1000")
    print(f"{one} = 1000")




name = input("Please enter yor name: ")
initial_deposit = float(input("Initial deposit: "))
account(name, initial_deposit = 0)
ph_denomination(balance)    