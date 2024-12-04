# Collections = single "variable" can used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER than List
# Set = {} unordered and immutable. But Add/Remove OK. No Duplications

var = {"orange", "pineapple", "smartphone", "coconut", "chair"}

print(dir(var))

# var.add() -> Add in the LIST or SET
# var.append() -> Add in the LIST or SET
# var.insert([index], 'item') -> Add in the LIST or SET on the index mentionated
# var.remove() -> Remove in the LIST or SET
# var.clear() -> Clear the COLLECTIONS
# var.pop() ->  Remove a RANDOM item in  SET    
# var.sort() -> Alphabetic COLLECTIONS
# var.reverse() -> Reverse the LIST or TUPLE
# var.index('item') -> show in what local are localized in LIST or TUPLE
# var.count('item') -> Count how many item have in LIST or TUPLE