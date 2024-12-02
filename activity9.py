def activity9():

	age = eval(input(" Enter your age: "))

	if age >= 1 and age <= 7 :
		print("Hi, your age is categorized as Toddler")

	elif age >= 8 and age <= 13 :
		print("Hi, your age is categorized as Pre-teen")

	elif age >= 14 and age <= 18 :
		print("Hi, your age is categorized as Teenager")

	elif age >= 19 and age <= 31 :
		print("Hi, your age is categorized as Early Adulthood")

	elif age >= 32 and age <= 45 :
		print("Hi, your age is categorized as Mid Adulthood")

	elif age >= 46 and age <= 59 :
		print("Hi, your age is categorized as Post Adulthood")

	elif age > 60 :
		print("Hi, your age is categorized as Senior")

	else :
		print("Invalid Age")