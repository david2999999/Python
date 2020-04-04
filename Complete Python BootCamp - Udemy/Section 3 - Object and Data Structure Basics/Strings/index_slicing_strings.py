my_string = 'Hello World'

print(my_string[0]) # H
print(my_string[8]) # r
print(my_string[9]) # l
print(my_string[-2]) # l

print(my_string[2:]) # llo World
print(my_string[:3]) # Hel
print(my_string[3:6]) # lo

print(my_string[::3]) # HlWl
print(my_string[2:7:2]) # HlWl

# Reversing a string in python
print(my_string[::-1])