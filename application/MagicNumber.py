def magic_number(num):
    mag_num = 0
    org_num = num
    length = len(str(num))
    for i in range(length, 0, -1):
        mag_num += (num % 10) ** i
        num = num // 10

    return mag_num == org_num


print(magic_number(89))

set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
set1.difference(set2)
