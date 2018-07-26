from sys import getsizeof


def perform_calc(num_str):
    a = 0
    b = 0
    is_plus_found = False

    for num in num_str:
        if num == '+':
            is_plus_found = True
            continue
        elif num == '=':
            print(type(a))
            print("Size of num_str: {} Bytes and length: {}".format(getsizeof(num_str), len(num_str)))
            print("Size of a: {} is {} Bytes".format(a, getsizeof(a)))
            print("Size of b: {} is {} Bytes".format(b, getsizeof(a)))
            print("Size of a + b: {} is {} Bytes".format(a + b, getsizeof(a)))
            return a + b
        elif num.isdigit():
            if is_plus_found:
                b = b * 10 + int(num)
            else:
                a = a * 10 + int(num)


def perform_string_calc(num_str):
    a = ""
    b = ""
    is_plus_found = False

    for num in num_str:
        if num == '+':
            is_plus_found = True
            continue
        elif num.isdigit():
            if is_plus_found:
                b = b + num
            else:
                a = a + num
    print("Size of a: {} is {} Bytes".format(a, getsizeof(a)))
    print("Size of b: {} is {} Bytes".format(b, getsizeof(a)))


text = "1233234234343434434342 + 123342342342423424 = "
print(perform_calc(text))
print("\n======================================================================================")
print(perform_string_calc(text))
