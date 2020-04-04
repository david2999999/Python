my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(2) # does not get added into the set

print(my_set)

my_list = [1, 1, 1, 1, 1, 2, 3, 3, 4]
print(set(my_list))

print(set('mississippi'))