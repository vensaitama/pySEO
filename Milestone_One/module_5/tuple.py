fruits = ('apple', 'banana', 'orange')
print(type(fruits))
access_tuple = fruits[2]
print(access_tuple)

# Tuple is Immutable (Unchangable)
# convert Tuple to List to Change or Add

fruits_new = list(fruits)
fruits_new[1] = "Cherry"
print(fruits_new)
print(type(fruits_new))
fruits = tuple(fruits_new)
print(type(fruits))