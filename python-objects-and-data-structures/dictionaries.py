# dictionaries are unordered sequence of key-value pair
my_dict = {
    "name": "rajib",
    "surname": "podder"
}
print(my_dict.keys())
print(my_dict["name"])
print(my_dict.items())
my_dict['age'] = 30
print(my_dict)
#Override exiting value
my_dict['surname'] = 'Podder'
print(my_dict)

##Iterate through dictionary
for keys,value in my_dict.items():
    print(f'{keys}=>{value}')
