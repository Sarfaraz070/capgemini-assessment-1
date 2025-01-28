l = list(map(int, input("Enter the numbers separated by space: ").split()))
if len(l) < 2:
    print("The list must have at least two numbers.")
else:
    max1, max2 = float('-inf'), float('-inf')
    for i in l:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    if max2 == float('-inf'):
        print("There is no second largest number (all elements are the same).")
    else:
        print(f"The second largest number is: {max2}")