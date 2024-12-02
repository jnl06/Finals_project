#creating function

def activity1():
    print("hello World")

def activity2():
    print("Hello World \nHello BSIT 1A") 

def activity3():
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    bday = input("Enter your bithday: ")       
    birthplace = input("Enter your birthplace: ")
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    fathers_name = input("Enter your fathers name: ")
    mothers_name = input("Enter your mothers name: ")
    address = input("Enter your address: ")
    civil_status = input("What is your civil status? ")
    relilgion = input("Enter your religion: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")

    print("My name is ", name , "a", age , "year/s old", gender, "born on ", bday , "in " + birthplace + ". I am " + height + " cm tall and weigh ", weight , "kg. ")

def activity4():
    pass

def activity5():
    pass

def activity6():
    #assignment operator
    x = 5

    print(f"piece{x}")

    x += 15 

    print(x)

    x += 10

    print(x)

def activity7():
    #conditional statement
    gold = 0

    name = input("Please enter your name: ")

    isGold = input("Is the mineral gold? ")

    if isGold.lower() == "yes" :
	    gold += 1
	    print(f"Hi {name}, the total number of gold you have is {gold}")

    else : 
	    print(f"The total number of gold you have is {gold}")

def activity8():
    password = input("Enter your password: ")

    if password.lower() == "secret" :
	    print("Access Granted")
	    print("Enjoy the system")

    elif password.lower() == "secret123" :
	    print("Access Granted") 
	    print("Enjoy the system")

    else : 
	    print("Access Denied")

    print("System Exit")

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

def activity10():
    name = input("Enter your name: ")
    student = input("Are you a student of DLL? (yes/no) : ")

    if student.lower() == "yes" :
	yearLevel = input("What year level are you? \nF - Freshmen \nJ- Junior \nS - Sophomore \nR - Senior \nYour answer: ")
	    if yearLevel.lower() == "f" :
		    print(f" Hi, {name} freshmen, Welcome to DLL")


	    elif yearLevel.lower() == "j" :
		    print(f" Hi, {name} junior, Welcome to DLL")

	    elif yearLevel.lower() == "s" :
		    print(f" Hi, {name} sophomore, Welcome to DLL")

	    elif yearLevel.lower() == "r" :
		    print(f" Hi, {name} senior, Welcome to DLL")

        else :
	        print("Thank you for using the system")

def activity11():
    #printing 10 times

    for cycle in range(1, 11):
        print("Hello world")

activity11()