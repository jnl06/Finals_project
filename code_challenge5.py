fahrenheit = eval(input("Enter a temperature in fahrenheit to convert into celsius: "))
celsius = ((fahrenheit - 32) * 5) / 9

print(f"{fahrenheit}°f is converted into {round(celsius, 2)}°C")