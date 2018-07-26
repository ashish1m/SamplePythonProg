def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    MOD = 10 ** 9 + 7

    res = 1
    exp = abs(n)

    for i in range(exp):
        res = (res * x) % MOD

    if n < 0:
        return 1 / res
    return res


base = float(input("Enter the base: "))
exp = int(input("Enter the exp: "))
print(myPow(base, exp))
print(base ** exp)
