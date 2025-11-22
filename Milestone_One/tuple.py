fruits = ("apple", "banana", "guave", "orange", "melon")
print(type(fruits))
print(fruits[2])

fruits = list(fruits)  #convert to list
print(type(fruits))

add_fruit = ["cherry", "lemon", "pineapple"]
fruits.extend(add_fruit)

fruits =tuple(fruits) #convert to tuple
print(fruits)