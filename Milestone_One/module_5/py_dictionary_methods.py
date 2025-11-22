bio_data = {
    "name" : "Santa Islam Runy",
    "DOB" : "Dec 07, 2005",
    "age" : 21,
    "hobby" : "Gardening",
    "country":"Bangladeshi"
}

# Access Elements
print(bio_data["name"])
print(bio_data.get("DOB"))

# Update Elements
bio_data["age"] = "20"
print(bio_data)

bio_data.update({"age":22}) # update
print(bio_data)

# Add elements
bio_data["Alive"] = True
bio_data.update({"Married": True})
print(bio_data)

# Delete Elements
del bio_data["Alive"]
print(bio_data)

# clear() ,popitem()

# items
x = bio_data.items()
print(x)