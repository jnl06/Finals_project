print("Enter 10 number \n------------------\n ")

n1 = 0

for i in range(1, 11):
    n2 = eval(input(f"Enter a number {i}: "))
    n1 += n2

print(f"\nThe total of the number you entered is {n1} ")    