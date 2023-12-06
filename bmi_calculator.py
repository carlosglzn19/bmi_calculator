height = input("Tell me your height in meters\n")

weight = input("Tell me your weight in kilograms\n")

bmi = int(weight) / (float(height)**2)

print("Your BMI is: " + str(bmi))