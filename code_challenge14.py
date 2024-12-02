def code_chal14():
    con = True
    num = 0
    print(f"Enter the number 0 to stop \n----------------------------")
    while con == True:
        numb = eval(input(f"Enter a number: "))
    
        if numb == 0:
            print(f"loop has terminated")
            print(f"The total of the number you enter is {num}")
            break
        
        else:
            num += numb
            continue            
    