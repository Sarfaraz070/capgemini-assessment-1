
def fact(n):
    if n == 0 or n == 1:  # Factorial of 0 and 1 is 1
        return 1
    else:
        return n * fact(n - 1)

p = int(input("Enter a number to calculate its factorial: "))
if p < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {p} is {fact(p)}")