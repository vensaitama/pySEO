numbers = [12, 4545, 54, 156,12,11,2,14,11,13,156, 111]

even = 0 # To get total even
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1 # To get total even
    else:
        odd += 1

print(f'Total Even is {even} and odd {odd}')