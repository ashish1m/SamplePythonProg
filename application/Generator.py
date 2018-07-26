def create_cubes(n):
    for x in range(n):
        yield (x ** 3)


def gen_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


gen_comp = (item * 4 for item in range(10))

for x in gen_comp:
    print(x)
