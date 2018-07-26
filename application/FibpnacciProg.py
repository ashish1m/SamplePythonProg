def fibonacci(num):
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b
    print()


num = int(input("Enter a number up to which you want fibonacci series: "))
fibonacci(num)