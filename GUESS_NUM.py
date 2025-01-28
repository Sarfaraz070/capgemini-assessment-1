import random
c=random.randrange(0,100)
trails=10
while trails>0:
    guess=int(input("Guess the number : "))
    if guess>c:
        print("Your Guess is higher than the target...")
        trails-=1
    elif guess<c:
        print("Your Guess is smaller than the target...")
        trails-=1
    else:
        print(f"YAY, You get the number in {trails} attempts..")
        trails-=1
        break
if trails==0:
    print(f"you Lost")