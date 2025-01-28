
n = int(input("ENTER THE NUMBER: "))
p = input("STRAIGHT OR REVERSE: ")

if p == 'STRAIGHT':
    for i in range(1, n+1):
        print("*" * i)
else:
    for i in range(n, 0, -1):
        print("*" * i)