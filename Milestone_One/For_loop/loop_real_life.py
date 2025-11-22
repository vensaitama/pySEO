# Write a Python program to count the number of even and odd numbers in a list of numbers

numbers = [12, 4545, 54, 156, 12,11,2,14,11,13, 156, 111]

even = 0
odd = 0
for i in numbers:
    if i % 2 == 0: # This condition finds the even or the odd
        even += 1 # This counts
    else:
        odd += 1 # This counts
print(f'Total Even {even}, Odd {odd}')


# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.



# Write a Python program to convert temperatures to and from Celsius and Fahrenheit.