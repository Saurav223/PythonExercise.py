import random

def rohanMul(choice):
    fake = random.randint(2,9)
    fakemul = []
    for i in range(1,11):
        if i == fake:
            fakemul.append(random.randint((choice * (i-1))+1,(choice * (i+1))-1))

        else:
            fakemul.append(i*choice)
    return fakemul

def check(lst):
    mul = lst[0]
    for i in range(1,11):
        if lst[i-1] != mul*i:
            print(f"Index {i} is incorrect")
            lst[i-1] = mul * i
    return lst


choices = int(input("Enter the multiplication you want:"))
lst = rohanMul(choices)
print(lst)
print(check(lst))

