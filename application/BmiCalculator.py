UNDER_WEIGHT_THRESHOLD = 18.5
OVER_WEIGHT_THRESHOLD = 25
OBESE_THRESHOLD = 30

height = int(input("Please enter your height (in cm): "))
weight = int(input("Please enter your weight (in kg): "))
while height == 0:
    height = int(input("Please enter proper height (in cm): "))

# converting from cm to m
height = height / 100
bmi = weight / (height ** 2)

print("<===========================>")
print("Your Body Mass Index (BMI) is: %.2f" % bmi)

if bmi < UNDER_WEIGHT_THRESHOLD:
    print("Hey! you are Under Weight. Consider consulting a doctor. :(")
elif UNDER_WEIGHT_THRESHOLD < bmi < OVER_WEIGHT_THRESHOLD:
    print("Hey Congrats! You have healthy weight. Keep it up. :)")
elif OVER_WEIGHT_THRESHOLD < bmi < OBESE_THRESHOLD:
    print("Hey! you are Over Weight. Consider consulting a doctor. :(")
else:
    print("Hey! you are Obese. Be serious against your health. Consider consulting a doctor immediately. :'(")
