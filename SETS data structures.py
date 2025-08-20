my_set={"apple","banana","cherry","date","banana"}
print(f"initial set:{my_set}")
my_set.add("grape")
print(f"after add ('grapes'):{my_set}")
my_set.remove("banana")
print(f"After remove('banana'): {my_set}")
set_lenght=len(my_set)
print(f"lenght of the set: {set_lenght}")
is_cherry_in_set="cherry" in my_set
print(f"Is 'cherry' in the sets? {is_cherry_in_set}")
is_mango_in_set="mango" in my_set
print(f"Is 'mango' in the sets? {is_mango_in_set}")
pooped_set_item=my_set.pop()
print(f"After pop():{my_set},Popped Item: {pooped_set_item}")
my_set.clear()
print(f"After clear(): {my_set}")