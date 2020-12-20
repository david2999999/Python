x = [1, 2, 3]
for item in x:
    # comment
    pass

my_string = 'Sammy'
for letter in my_string:
    if letter == 'a':
        continue
    print(letter)

print("======")

for letter in my_string:
    if letter == 'a':
        break
    print(letter)

print("======")

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1