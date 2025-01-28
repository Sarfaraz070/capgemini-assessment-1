password = input("Enter your password: ")
digit_count = 0
uppercase_count = 0
letter_count = 0
special_count = 0

if len(password) < 8:
    print(f"Your password needs at least {8 - len(password)} more characters.")
else:
    for char in password:
        if char.isdigit():
            digit_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isalpha():
            letter_count += 1
        elif not char.isalnum():
            special_count += 1

    if digit_count > 0 and uppercase_count > 0 and letter_count > 0 and special_count > 0:
        print("Your password is secure.")
    else:
        print("Your password is not secure.")