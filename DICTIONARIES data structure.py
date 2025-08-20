my_dictionary={"brand":"Ford","model":"Mustang","year":"1964","color":"red"}
print(f"initial Dictionary:{my_dictionary}")
model_name=my_dictionary["model"]
print(f"Model:{model_name}")
year_value=my_dictionary["year"]
print(f"year:{year_value}")
all_keys=my_dictionary.keys()
print(f"All keys: {list(all_keys)}")
all_values=my_dictionary.values()
print(f"All values: {list(all_values)}")
all_items=my_dictionary.items()
print(f"All items: {list(all_items)}")
my_dictionary["engiene"]="V8"
print(f"after adding 'engine':{my_dictionary}")
my_dictionary["color"]="blue"
print(f"after changing 'color':{my_dictionary}")
removed_year=my_dictionary.pop("year")
print(f"after pop('year'):{my_dictionary}, removed year {removed_year}")
del my_dictionary["brand"]
print(f"after del my_dictionary['brand']:{my_dictionary}")
dictionary_lenght=len(my_dictionary)
print(f"Lenght of the dictionary: {dictionary_lenght}")
my_dictionary.clear()
print(f"After clear(): {my_dictionary}")
