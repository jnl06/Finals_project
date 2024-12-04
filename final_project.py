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

#from activity19 import activity19
#from activity20 import activity20
#from activity21 import activity21
#from activity22 import activity22

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
print(f"Hello {name}")

con = True

while con:
    choice = input("\nWhat would you like to open?\n1 - Activities \n2 - Code Challenges \n0 - Exit\nYour answer: ")
    
    if choice == "1":
        while True:
            print("0 - Return to the main menu")
            print("1 - Print function")
            print("2 - ")
            act_num = input("\nSelect activity to open:")
            
            if act_num == "1":
                print("This is our activity 1")
                print("=========================")
                activity1()
            elif act_num == "2":
                activity2()
            elif act_num == "3":
                activity3()
            elif act_num == "4":
                activity4()
            elif act_num == "5":
                activity5()
            elif act_num == "6":
                activity6()
            elif act_num == "7":
                activity7()
            elif act_num == "8":
                activity8()
            elif act_num == "9":
                activity9()
            elif act_num == "10":
                activity10()
            elif act_num == "11":
                activity11()
            elif act_num == "12":
                activity12()
            elif act_num == "13":
                activity13()
            elif act_num == "14":
                activity14()
            elif act_num == "15":
                activity15()
            elif act_num == "16":
                activity16()
            elif act_num == "17":
                activity17()
            elif act_num == "18":
                activity18()
            elif act_num == "0":
                break  # Return to main menu
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":
        while True:
            chal_num = input("\nSelect code challenge to open (Enter 0 to return to main menu): ")
            
            if chal_num == "1":
                code_chal1()
            elif chal_num == "2":
                code_chal2()
            elif chal_num == "4":
                code_chal4()
            elif chal_num == "5":
                code_chal5()
            elif chal_num == "6":
                code_chal6()
            elif chal_num == "7":
                code_chal7()
            elif chal_num == "8":
                code_chal8()
            elif chal_num == "9":
                code_chal9()
            elif chal_num == "10":
                code_chal10()
            elif chal_num == "11":
                code_chal11()
            elif chal_num == "12":
                code_chal12()
            elif chal_num == "13":
                code_chal13()
            elif chal_num == "14":
                code_chal14()
            elif chal_num == "15":
                code_chal15()
            elif chal_num == "16":
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
