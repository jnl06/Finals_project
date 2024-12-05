def activity18():

    tri = eval(input(" Enter number of triangle(s): "))

    for x in range(1, 6):
        for y in range(1, tri + 1):
            for z in range(1, x+1):
                print("*", end=" ")
            for a in range(5, x, -1):
                print(" ", end=" ")  
            print(end=" ")      
        print()     
            