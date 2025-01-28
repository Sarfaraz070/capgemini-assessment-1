
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"

n = input("Enter a string or number: ")
print(is_palindrome(n))