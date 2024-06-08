import random

def select(a,b):
    choices = random.randint(a,b)
    return choices

def check(x):
    i = 0
    while True:
        y = int(input(f"Enter your guess player {(i%2)+1}:"))
        if x < y:
            print("Guess Smaller Number")

        elif x > y:
            print("Guess Higher Number")

        else:
            print("You guess is correct")
            print(f"Player {(i%2)+1} Win")
            break
        i += 1

print("******WElCOME TO GUESS THE NUMBER GAME*****")
print("Enter the range of number")
a = int(input("Lower Number:"))
b = int(input("Higher Number:"))
check(select(a,b))




        


