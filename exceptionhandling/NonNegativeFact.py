def fact_calc(num):
    if num < 0:
        raise ValueError("Negative value error")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * fact_calc(num - 1)


run = True
while run:
    str = input("Enter number to calculate factorial(x for exit): ")
    if str.lower() == 'x':
        run = False
    else:
        print("Factorial of %s is %d" % (str, fact_calc(int(str))))

print("Program ended")
