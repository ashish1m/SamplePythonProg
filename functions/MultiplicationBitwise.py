def multiply(a, b):
    result = 0
    while b > 0:
        if b & 1:
            result = result + a
        a = a << 1
        b = b >> 1

    return result


print(multiply(12379827, 27892729))
