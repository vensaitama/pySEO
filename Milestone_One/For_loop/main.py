birthday = ['Motu', 'Patlu', 'Boltu', "Poltu", 'Haris']

# print('Happy Birthday,',birthday[0])
# print('Happy Birthday,',birthday[1])
# print('Happy Birthday,',birthday[2])
# print('Happy Birthday,',birthday[3])
# print('Happy Birthday,',birthday[4])

# for i in birthday:
#     print("Happy Birthday,", i)

print(len(birthday))


i = 0
while i < len(birthday):
    print('Happy Birhtday', birthday[i])
    i = i + 1

# initial value
# i = 0
# condition
# while i < 5:
# code block (loop body)
#     print(i)
# update statement
#     i += 1

# --------------------------------
# Wishing happy Birhtday
wish_hb = ['Hamim', 'Halim', 'Habib', 'Hasib', 'Haris', 'Hanif', 'Harun']

#print(len(wish_hb)) 
# Here len(wish_hb) counts the total number of people in the list 
i = 0 # initial value
while i < len(wish_hb): # condition + loop body
    print('Happy Birthday', wish_hb[i]) 
    # wish_hb prints the list
    # [number] access the list
    # i declars which number to print from list (here e.g. 0, 1, 2, 3, 4, 5, 6)
    i += 1 # updates statement
