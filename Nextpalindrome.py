def reverse(int):
    tmp = 0
    while int > 0:
        tmp = tmp * 10 + int % 10
        int = int // 10
    return tmp

def Nextpalin(int):
    tmp = int
    while tmp != reverse(tmp):
        tmp +=1
    if int == tmp:
        print(f"{int} is its self a palindrome")

    else:
        print(f"The next palindrome of {int} is {tmp}")

num = int(input("Enter a number"))
Nextpalin(num)