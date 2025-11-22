fruit = [
    "apple",
    "banana",
    "berry",
    "lichi",
    "mango"
]

print(type(fruit))
print(fruit[1].capitalize())


fruit[1] = "Jack fruit"
print(fruit)

fruit.append("Mula")  
print(fruit)

fruit.insert(1, "Pineapple")
print(fruit)

new_fruit = ["papaya", "tomato"]
fruit.extend(new_fruit)
print(fruit)


num_01 = [1,2,3,4,5,6,7,8]
num_02 = [11,22,33,44,55,66,77,88]
new_num = num_01 + num_02
print(new_num)

sesnl_fruit = fruit
sesnl_fruit.remove("tomato")
print(sesnl_fruit)
