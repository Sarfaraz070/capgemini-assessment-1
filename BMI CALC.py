
def BMI(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return f"Underweight. Your BMI is {bmi:.2f}"
    elif 18.5 <= bmi < 24.9:
        return f"Normal weight. Your BMI is {bmi:.2f}"
    elif 25 <= bmi < 29.9:
        return f"Overweight. Your BMI is {bmi:.2f}"
    else:
        return f"Obese. Your BMI is {bmi:.2f}"
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
