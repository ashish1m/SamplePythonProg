from collections import OrderedDict

normal_dict = dict()
normal_dict['a'] = 1
normal_dict['b'] = 2
normal_dict['c'] = 3
normal_dict['d'] = 4
normal_dict['e'] = 5

print("Normal dict: ")
for k, v in normal_dict.items():
    print(k, v)

print()
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print("Ordered dict: ")
for k, v in ordered_dict.items():
    print(k, v)

# two normal dict with same key value pair will always be equal
a = dict()
a['a'] = 1
a['b'] = 2

b = dict()
b['b'] = 2
b['a'] = 1

print("Is normal dict a and b equal:", a == b)

# two ordered dict with same key value pair will never be equal if they have different order
a = OrderedDict()
a['a'] = 1
a['b'] = 2

b = OrderedDict()
b['b'] = 2
b['a'] = 1

print("Is OrderedDict a and b equal:", a == b)
