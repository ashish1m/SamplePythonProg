"""
# === Arithmetic operator ===
num1 = 10
num2 = 3

print("Num1 + Num2 =", num1 + num2)
print("Num1 - Num2 =", num1 - num2)
print("Num1 * Num2 =", num1 * num2)
print("Num1 / Num2 =", num1 / num2)

# exponential
print("Num1 ^ Num2 =", num1 ** num2)
# modulus
print("Num1 % Num2 =", num1 % num2)
# floor division
print("Num1 // Num2 =", num1 // num2)


# === Assignment operator ===
num3 = num1 + num2
print("Num3 =", num3)

num3 += num2
print("Num3 =", num3)


# === Comparison operator ===
print("Num1 < Num2 =", num1 < num2)
print("Num1 > Num2 =", num1 > num2)
print("Num1 == Num2 =", num1 == num2)
print("Num1 != Num2 =", num1 != num2)

# === Logical operator ===
x = True
y = False
print("x and y", x and y)
print("x or y", x or y)
print("not x", not x)

# === Bitwise & Identity operator ===
num4 = 6
num5 = 3
print("Num4 & Num5 =", num4 & num5)
print("Num4 | Num5 =", num4 | num5)
print("Num4 ^ Num5 =", num4 ^ num5)
print("Num4 >> Num5 =", num4 >> num5)
print("Num4 << Num5 =", num4 << num5)
print("Num4 is Num5 =", num4 is num5)
print("Num4 is not Num5 =", num4 is not num5)
"""

# === Membership operator ===
list1 = [1, 2, 3, 4, 5]
checkNum = 3
checkNotNum = 10
print("checkNum in list1 =", checkNum in list1)
print("checkNotNum in list1 =", checkNotNum in list1)

