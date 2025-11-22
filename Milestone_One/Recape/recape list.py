fruits = ['apple', 'banana', 'orange']
print(type(fruits))
print(fruits[1])
fruits[1] = 'cherry'
print(fruits)

fruits.append('papaya')
print(fruits)

fruits.insert(1, "avocado")
print(fruits)


# Connect two lists
number = [1,2,3,4,5]
number_two = [6,7,8,9]
number.extend(number_two)
print(number)


# Concate
class_one = ['Robin', 'Hamim', 'Momita', 'Runy', 'Zyan']
class_two = ['Sanjan', 'Naushin', 'Oysie', 'Jisan']
people = class_one + class_two
print(people)

# Removal

class_two.remove('Jisan')
print(class_two)
class_two.pop()
print(class_two)
class_two.pop(1)
print(class_two)

