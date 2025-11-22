# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

tem = input("Enter Temperature 10F, 30C: ")
degree = int(tem[:-1])
unit = tem[-1]
print(degree, unit)

if unit.upper() == "C":
    result = degree * 1.8 + 32
    unit = "Fahrenheit"
elif unit.upper() == "F":
    result = (degree -32) * (5/9)
    unit = "Celcius"
else:
    print("Enter Valid Value eg. 10F, 30C")
    quit()
print (result, unit)