family = {
    "father" : 65,
    "mother" : 55,
    "children" : 35
}
print(type(family)) #<class 'dict'>
print(family.get("mother"))
family.update({"mother": 60})
print(family)

family["grandmother"] = 80
print(family)

family.update({"grandmother":70})
print(family)