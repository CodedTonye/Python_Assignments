#-Get weight and height as decimal numbers
#-Calculate BMI
#-Determine category
#-Display results

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))


bmi = weight / (height * height)


if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
elif bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")
