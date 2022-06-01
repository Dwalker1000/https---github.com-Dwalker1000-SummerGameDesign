import os
os.system('cls')

weight = int(input("input your weight in pounds: "))
height = int(input("input your height in inches: "))

BMI = round(weight / (height * height) * 703, 2)
print("Your BMI is: ", BMI)

if(BMI < 14.5):
    print("your underweight")

if(BMI > 40):
    print("your overwieght")