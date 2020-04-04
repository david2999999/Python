t = (1, 2, 3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))
print(len(t))
###################################
t = ('one', 2)
print(t[0])
print(t[-1])

t = ('a', 'a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print(t.index('b'))
###################################
t = (1, 2, 3)
my_list = [1, 2, 3]

my_list[0] = 'NEW'
print(my_list)