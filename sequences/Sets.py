integer = {1, 2, 3, 4, 5}
print(integer)

# discarding a value
integer.discard(4)
print(integer)

# union
real = {1, 2, 4, 7, 8, 9}
print(integer | real)

# intersection
print(integer & real)

# difference
print(integer - real)

# XOR
print(integer ^ real)

# conversion to list
integer_list = list(integer)
print(integer_list)
