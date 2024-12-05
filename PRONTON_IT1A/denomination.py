name = input("Enter your name: ")
amount  = eval(input("Enter the amount to deposit: "))

print("Hi, " + name + " the amount you deposit is distributed in PH denomination is as follows: ")

one_thousand = amount // 1000
n1 = amount % 1000
five_hundred = n1 // 500
n2 = n1 % 500
two_hundred = n2 // 200
n3 = n2 % 200
one_hundred = n3 // 100
n4 = n3 % 100
fifty = n4 // 50
n5 = n4 % 50
twenty = n5 // 20 
n6 = n5 % 20
ten = n6 // 10
n7 = n6 % 10
one = n7 // 1

print(int(one_thousand), "- 1000")
print(int(five_hundred), "- 500")
print(int(two_hundred), "- 200")
print(int(one_hundred), "- 100")
print(int(fifty), "- 50")
print(int(twenty), "- 20")
print(int(ten), "- 10")
print(int(one), "- 1")