import random

# num = int(input("Enter the number to be found: "))
n = 100
num = int(random.random() * n) + 1
for value in range(50):
    if value == num:
        print("Found it!")
        break
else:
    print("Nowhere to be found. :-(")
