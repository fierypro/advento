weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))/100

bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("obese")
