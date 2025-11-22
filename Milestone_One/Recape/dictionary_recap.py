family={
    "father": 50,
    "mother": 45,
    "children": 25
}
print(type(family)) # <class 'dict'>
print(family["mother"]) #access

# Mother age correction
family["mother"] = 44
print(family)


# Adding item into the dictionary
family["grandpa"] = 80
print(family)

# Remove item
family.pop("grandpa")
print(family)

print(family.get("father"))