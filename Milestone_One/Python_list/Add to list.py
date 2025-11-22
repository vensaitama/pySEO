students = ["Robi", "Chobi", "Hafsa", "Runy"]
students.insert(1, "Kobir")
print(students)


fruits = ["apple", "banana", "cherry", "berry"]
fruits.extend(["Guava"])
print(fruits)


characters = True
actors_list = ["Sakib", "Manna", "Riaz"]
actress_list = ["Opu", "Sabnur", "Sabana"]
actors_list.extend(actress_list)
characters = actors_list
print(characters)