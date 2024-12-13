#importing codes
#activities
from activity1 import activity1
from activity2 import activity2
from activity3 import activity3
from activity4 import activity4
from activity5 import activity5
from activity6 import activity6
from activity7 import activity7
from activity8 import activity8
from activity9 import activity9
from activity10 import activity10
from activity11 import activity11
from activity12 import activity12
from activity13 import activity13
from activity14 import activity14
from activity15 import activity15
from activity16 import activity16
from activity17 import activity17
from activity18 import activity18
from activity19 import activity19
from activity20 import activity20
from activity21 import activity21
from activity22 import activity22
from activity23 import activity23
from activity24 import activity24
from activity25 import activity25

#code challenges
from code_challenge1 import code_chal1
from code_challenge2 import code_chal2
from code_challenge4 import code_chal4
from code_challenge5 import code_chal5
from code_challenge6 import code_chal6
from code_challenge7 import code_chal7
from code_challenge8 import code_chal8
from code_challenge9 import code_chal9
from code_challenge10 import code_chal10
from code_challenge11 import code_chal11
from code_challenge12 import code_chal12
from code_challenge13 import code_chal13
from code_challenge14 import code_chal14
from code_challenge15 import code_chal15
from code_challenge16 import code_chal16

print("Activities and Code Challenges")
print("==============================\n")

name = input("Please enter your name: ")
print("-----------------------------\n")
print(f"Hello {name}, welcome to the compilation program")

con = True

while con:
    choice = input("\nWhat would you like to open?\n1 - Activities \n2 - Code Challenges \n0 - Exit\nYour answer: ")
    
    if choice == "1":
        while True:
            print("\n0 - Return to the main menu")
            act_num = input("\nSelect one activity to open (1 - 25): ")
            print()
            if act_num == "1":
                print("This is Activity 1\n---------------------")
                activity1()
            elif act_num == "2":
                print("This is Activity 2\n---------------------")
                activity2()
            elif act_num == "3":
                print("This is Activity 3\n---------------------")
                activity3()
            elif act_num == "4":
                print("This is Activity 4\n---------------------")
                activity4()
            elif act_num == "5":
                print("This is Activity 5\n---------------------")
                activity5()
            elif act_num == "6":
                print("This is Activity 6\n---------------------")
                activity6()
            elif act_num == "7":
                print("This is Activity 7\n---------------------")
                activity7()
            elif act_num == "8":
                print("This is Activity 8\n---------------------")
                activity8()
            elif act_num == "9":
                print("This is Activity 9\n---------------------")
                activity9()
            elif act_num == "10":
                print("This is Activity 10\n---------------------")
                activity10()
            elif act_num == "11":
                print("This is Activity 11\n---------------------")
                activity11()
            elif act_num == "12":
                print("This is Activity 12\n---------------------")
                activity12()
            elif act_num == "13":
                print("This is Activity 13\n---------------------")
                activity13()
            elif act_num == "14":
                print("This is Activity 14\n---------------------")
                activity14()
            elif act_num == "15":
                print("This is Activity 15\n---------------------")
                activity15()
            elif act_num == "16":
                print("This is Activity 16\n---------------------")
                activity16()
            elif act_num == "17":
                print("This is Activity 17\n---------------------")
                activity17()
            elif act_num == "18":
                print("This is Activity 18\n---------------------")
                activity18()
            elif act_num == "19":
                print("This is Activity 19\n---------------------")
                activity19()
            elif act_num == "20":
                print("This is Activity 20\n---------------------")
                activity20()
            elif act_num == "21":
                print("This is Activity 21\n---------------------")
                activity21()
            elif act_num == "22":
                print("This is Activity 22\n---------------------")
                activity22()
            elif act_num == "23":
                print("This is Activity 23\n---------------------")
                activity23()
            elif act_num == "24":
                print("This is Activity 24\n---------------------")
                activity24()
            elif act_num == "25":
                print("This is Activity 25\n---------------------")
                activity25()
            elif act_num == "0":
                break 
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            print("\n0 - Return to the main menu")
            chal_num = input("\nSelect one code challenge to open (1 - 16): ")
            print()
            if chal_num == "1":
                print("This is Code Challenge 1\n---------------------")
                code_chal1()
            elif chal_num == "2":
                print("This is Code Challenge 2\n---------------------")
                code_chal2()
            elif chal_num == "3":
                print("This is Code Challenge 3\n---------------------")
                activity3()
            elif chal_num == "4":
                print("This is Code Challenge 4\n---------------------")
                code_chal4()
            elif chal_num == "5":
                print("This is Code Challenge 5\n---------------------")
                code_chal5()
            elif chal_num == "6":
                print("This is Code Challenge 6\n---------------------")
                code_chal6()
            elif chal_num == "7":
                print("This is Code Challenge 7\n---------------------")
                code_chal7()
            elif chal_num == "8":
                print("This is Code Challenge 8\n---------------------")
                code_chal8()
            elif chal_num == "9":
                print("This is Code Challenge 9\n---------------------")
                code_chal9()
            elif chal_num == "10":
                print("This is Code Challenge 10\n---------------------")
                code_chal10()
            elif chal_num == "11":
                print("This is Code Challenge 11\n---------------------")
                code_chal11()
            elif chal_num == "12":
                print("This is Code Challenge 12\n---------------------")
                code_chal12()
            elif chal_num == "13":
                print("This is Code Challenge 13\n---------------------")
                code_chal13()
            elif chal_num == "14":
                print("This is Code Challenge 14\n---------------------")
                code_chal14()
            elif chal_num == "15":
                print("This is Code Challenge 15\n---------------------")
                code_chal15()
            elif chal_num == "16":
                print("This is Code Challenge 16\n---------------------")
                code_chal16()
            elif chal_num == "0":
                break  
            else:
                print("Invalid choice. Please try again.")
    
    elif choice == "0":
        print("\nExiting the program. Goodbye!")
        con = False  
    
    else:
        print("Invalid choice. Please select again.")
