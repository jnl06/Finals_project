grocery = input("Did you buy a grocery? (yes/no): ")

if grocery.lower() == "yes" :
    item = input("Name of the item: ")
    price = eval(input("Price of the item: "))
    age = eval(input("What is your age? "))
    amount = eval(input("Enter the amount given: "))
    tax = price * 0.123
    total = price + tax
    change = amount - total
    print(f"Hi customer you purchased a {item}, with a price of {price} plus 12.3% tax ({round(tax, 2)}), total of {round(total, 2)}")
    if age >= 60 :
        discount = total * 0.52
        print("Your age is categorized as senior, then you will get a 5.2% discount")
        discounted = total - discount
        change = amount - discounted
        print(f"Amount given : {amount} ")
        print(f"Change: {round(change, 2)}")
    else :
        print(f"Amount given : {amount} ")
        print(f"Change: {round(change, 2)}")
        
else :
    print("Thank you for using the system")