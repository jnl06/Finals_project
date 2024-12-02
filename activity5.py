def activity5():
    print("Fahrenheit to Celsius Converter")
    print("===============================")

    fh = eval(input("Enter temperature in fahreheit: "))

    cl = ((fh - 32) * 5) / 9

    print(f"{fh} degreed fahreheit converted to celsius is {round(cl, 2)}")