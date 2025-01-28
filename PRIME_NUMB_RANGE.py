import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the first prime number: "))
end = int(input("Enter the second prime number: "))

start_is_prime = is_prime(start)
end_is_prime = is_prime(end)

print(f"Is {start} prime? {start_is_prime}")
print(f"Is {end} prime? {end_is_prime}")

if start_is_prime and end_is_prime:
    print("Both numbers are prime.")
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
else:
    print("Both numbers are not prime.")