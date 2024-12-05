grocery = input("Did you buy a grocery? (yes/no) ")

if grocery.lower() == "yes" :
	item = input("Name of the item: ")
	price = eval(input("Price of the item: "))
	age = eval(input("What is your age? "))
	given = eval(input("Amount given: "))
	tax = price * 0.123
	total = price + tax
	
	if age >= 60 :
		discount = total * 0.052 
		ntotal = total - discount 
		print(f"You are eligible for senior discount")
		