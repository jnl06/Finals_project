def code_chal4():
    number1 = eval(input("Enter the first number: "))
    number2 = eval(input("Enter the second number: "))

    answer1 = number1 + number2
    answer2 = number1 - number2
    answer3 = number1 * number2
    answer4 = number1 / number2
    answer5 = number1 % number2
    answer6 = number1 ** number2
    answer7 = number1 // number2

    print("The sum of", number1, "+", number2, "is", answer1)
    print("The difference between of", number1, "and", number2, "is", answer2)
    print("The product of", number1, "and", number2, "is", answer3)
    print("The quotient of", number1, "and", number2, "is", answer4)
    print("The remainder of", number1, "and", number2, "is",answer5)
    print(number1, "exponent by", number2, "is", answer6)
    print("The floor division of", number1 , "and" , number2 , "is", answer7)