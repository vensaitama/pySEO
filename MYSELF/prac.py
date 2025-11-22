# initial value 
i = 0
#condition
while i < 5:
    # loop body
    print(i)
    #update statement
    i += 1

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


i = 0
while i<30: # means if i is less then <30, u should loop until the end of 30 which is 0-29
    print(i) # print if condition is true
    i += 1 #add a number with condition, like 0 <30, 1 <30, 2 <30 till 29<30. 
    # the loop stops at 29<30. 
    # without i += 1 it will nonstop loops


    final_number = int(input("Enter a number: "))
    v = 0
    while v < final_number:
        print(v)
        v += 1

