# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

i = 0
while i <= 6:
    if i == 3 or i == 6:
        i += 1
        continue
    print(i)
    i += 1


numbers = [0,1,2,3,4,5,6]
for i in numbers:
    if i ==3 or i ==6:
        continue
    print(i)