from collections import namedtuple

# normal tuple
t = (1, 2, 3, 4, 5, 6)
print(t[0])

# named tuple
Dog = namedtuple('Dog', 'name age breed')
sam = Dog('Sammy', 3, 'Lab')
tom = Dog('Tommy', 2, 'Pug')
print(tom)
