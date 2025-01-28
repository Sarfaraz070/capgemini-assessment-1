
l = list(map(int, input("Enter the numbers separated by space: ").split()))
e = [i for i in l if i % 2 == 0]  # List comprehension for even numbers
o = [i for i in l if i % 2 != 0]  # List comprehension for odd numbers
print(f"Even List: {e}")
print(f"Odd List: {o}")