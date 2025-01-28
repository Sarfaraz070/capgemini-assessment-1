
n = int(input("Enter the year you want to check: "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")