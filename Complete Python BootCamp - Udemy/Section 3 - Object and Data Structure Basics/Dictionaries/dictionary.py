my_dict = {'key1':'value1', 'key2':'value2'}

print(my_dict['key1'])

prices_lookup = {
    'apple': 2.99,
    'oranges': 1.99,
    'milk': 5.80
}

print(prices_lookup['apple'])

d = {
    'k1': 123,
    'k2': [0, 1, 2],
    'k3': {
        'inside': 100
    }
}

print(d['k1'])
print(d['k2'])
print(d['k2'][2])
print(d['k3'])
print(d['k3']['inside'])

d = {
    'key1': ['a', 'b', 'c']
}

print(d['key1'][2].upper())

d = {
    'k1': 100,
    'k2': 200
}

d['k3'] = 300
print(d)

if 'k4' not in d:
    print("K4 is not in dictionary")

print(d.keys())
print(d.values())
print(d.items())