# Task: The user will give two numbers. The code must identify the bigger number.

# x = int(input("Enter your first number:\t"))
# y = int(input("Enter your second number:\t"))
# if x > y:
#     print("x is bigger than y")
# elif x == y:
#     print("x  and y are same")
# else:
#     print("x is smaller than y")

#-----------------------------
# completed = True
# if completed:
#     print("https://celebheights.com")
# else:
#     print("I don't know this")
#--------------------------------
name = input("Enter celebrity name:\t")
celeb_height = float(input("Enter the height in cm:\t"))
celeb_height_meter = celeb_height / 100
celeb_height_inches = round(celeb_height / 2.54, 2)

celeb_height_feet = celeb_height_inches // 12
remaining_celeb_inches = celeb_height % 12

print(name + "s' Height")
# print(name+"'s Height in Centimeter " + str(celeb_height))
# print(name+"'s Height in Meter " + str(celeb_height_meter))
# print(name+"'s Height is Inches " + str(celeb_height_inches))
print(name+"'s Height in Centimeter " + str(celeb_height) + ", in Meter "+ str(celeb_height_meter) + ", in Inchec "+ str(celeb_height_inches) )
print(name + "s' Height"+ celeb_height_feet, "Feet", remaining_celeb_inches, "Inches")