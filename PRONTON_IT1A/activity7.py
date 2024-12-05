#conditional statement
def activity7():
	gold = 0

	name = input("Please enter your name: ")

	isGold = input("Is the mineral gold? ")

	if isGold.lower() == "yes" :
		gold += 1
		print(f"Hi {name}, the total number of gold you have is {gold}")

	else : 
		print(f"The total number of gold you have is {gold}")