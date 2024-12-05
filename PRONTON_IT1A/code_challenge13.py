for x in range(4, 0, -1):
    for y in range(x):
        print(" ", end=" ")
    for z in range(1, 5):
        print(z, end=" ") 
    for a in range(x, 5):
        print("^", end=" ")        
    print()