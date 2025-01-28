
s = input()
s = s.lower()  # Correctly assigning the lowercase string back to s
vowels = 'aeiou'
consonent = 'bcdfghjklmnpqrstvwxyz'
d = 0  # count of digits
a = 0  # count of non-alphanumeric characters
o = 0  # count of vowels
c = 0  # count of consonants

for i in range(len(s)):
    if s[i].isdigit():
        d += 1
    elif s[i] in vowels:
        o += 1
    elif s[i] in consonent:
        c += 1
    else:
        a += 1

print(f"Vowels : {o}  Consonants : {c} Alphanumeric : {a} Numbers : {d}")