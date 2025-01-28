def Grade(a, b, c, d, e):
    total = a + b + c + d + e
    percentage = (total / 500) * 100
    
    if percentage >= 80:
        return f"You got A Grade with {percentage:.2f}% and total marks you got is {total}"
    elif percentage >= 70:
        return f"You got B Grade with {percentage:.2f}% and total marks you got is {total}"
    elif percentage >= 65:
        return f"You got C Grade with {percentage:.2f}% and total marks you got is {total}"
    elif percentage >= 55:
        return f"You got D Grade with {percentage:.2f}% and total marks you got is {total}"
    elif percentage >= 45:
        return f"You got E Grade with {percentage:.2f}% and total marks you got is {total}"
    elif percentage >= 35:
        return f"You got P Grade with {percentage:.2f}% and total marks you got is {total}"
    else:
        return f"You got F Grade with {percentage:.2f}% and total marks you got is {total}"

# Input marks
t = int(input("Enter your marks in Telugu: "))
w = int(input("Enter your marks in English: "))
z = int(input("Enter your marks in Maths: "))
x = int(input("Enter your marks in Science: "))
m = int(input("Enter your marks in Social: "))

# Print grade
print(Grade(t, w, z, x, m))