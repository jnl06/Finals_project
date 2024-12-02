n1 = 0
print(f"Enter 10 number\n-------------------\n ")

for i in range(1, 11):
    n2 = eval(input(f"Enter a number {i}: "))
    n1 += n2
    
  
print(f"The total of the numbers you entered is {n1}")