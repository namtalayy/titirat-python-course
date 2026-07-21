# BMI Calculator

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

height_meter = height / 100
bmi = weight / (height_meter ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25.0:
    category = "Normal weight"
elif bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"
    
print(f"Your BMI is: {bmi:.1f}")
print(f"Your BMI Category: {category}")