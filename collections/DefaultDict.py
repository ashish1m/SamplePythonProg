from collections import defaultdict

# using normal dictionary
d = {'k1': 1}
print(d['k1'])

# now if we try to access not existing key
try:
    d['k2']
except KeyError:
    print("Key doesn't exist")

# we use defaultdict never raises KeyError
d = defaultdict(lambda: 0)
print(d['one'])
print(d['two'])

print(d.items())
