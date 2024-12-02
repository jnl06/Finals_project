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
choice = input("What would you like to open?\n1 - Activities \n2 - Code Challenges \nYour answer:")
con = True

while con:
    if choice == "1":
        act_num = input("Select activity to open: \n1 - ")
        if act_num == "1":
            activity1()
            continue
            
        elif act_num == "2":
            activity2()
            continue
            
        elif act_num == "3":
            activity3()
            continue    
            
        elif act_num == "4":
            activity4()
            continue
            
        elif act_num == "5":
            activity5()
            continue
            
        elif act_num == "6":
            activity6()
            continue
            
        elif act_num == "7":
            activity7()
            continue
            
        elif act_num == "8":
            activity8()
            continue
            
        elif act_num == "9":
            activity9()
            continue
            
        elif act_num == "10":
            activity10()
            continue
            
        elif act_num == "11":
            activity11()
            continue
            
        elif act_num == "12":
            activity12()
            continue
            
        elif act_num == "13":
            activity13()
            continue
            
        elif act_num == "14":
            activity14()
            continue
            
        elif act_num == "15":
            activity15()
            continue
            
        elif act_num == "16":
            activity16()
            continue
            
        elif act_num == "17":
            activity17()
            continue
            
        elif act_num == "18":
            activity18()
            continue
            
        elif act_num == "19":
            activity19()
            continue
            
        elif act_num == "20":
            activity20()
            continue
            
        elif act_num == "21":
            activity21()
            continue
            
        elif act_num == "22":
            activity22()
            continue
            
        elif act_num == "0":
            return choice
            
        else:
            print("Invalid Choice")
            break
            
            