def code_chal15():
    import os

    con = True
    no = 0

    while con:
        ask = input("Do you wish to create a new triangle (yes or no): ")

        if ask.lower() == "no":
            print("program / loop terminated")
            break

        elif ask.lower() == "yes":
            os.system("cls")
            no += 1
            for x in range(1, 6):
                for r in range(1,no + 1):
                    for y in range(1,x+1):
                        print("*", end=" ")
                    for z in range(6, x, -1):
                        print(" ", end=" ")
                    print(end=" ")    
                print()
            continue        

        else:
            os.system("cls")
            print("Invalid answer, please only answer 'yes' or 'no")
            continue