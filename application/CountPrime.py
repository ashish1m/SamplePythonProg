def countPrime(num):
    if num < 2:
        return 0

    prime = [2]

    # start the count from 3
    x = 3

    while x <= num:
        for y in prime:
            if x%y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2

    print("List of prime numbers:", prime)

    return len(prime)


num = int(input("Enter the number: "))
print("Total number of prime nos:", countPrime(num))
