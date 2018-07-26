def fib(n, lookup):

    #base case
    if n == 0 or n == 1:
        lookup[n] = n

    # if lookup doesn't have solution
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    print(lookup[n])
    return lookup[n]


n = 10
lookup = [None] * 100
fib(n, lookup)