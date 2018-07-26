def get_array_address(r, c):
    base = 100
    item_size = 2
    row = 4
    col = 4

    address_of_item = base + r * (row * item_size) + c * item_size
    return address_of_item


row = int(input("Row: "))
col = int(input("Col: "))
print(get_array_address(row, col))
