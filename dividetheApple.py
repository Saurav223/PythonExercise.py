def apple(n,mn,mx):
    for i in range(mn,mx+1):
        if n % i == 0:
            print(f"{i} is the divisor of {5}")

n = int(input('Enter the number of apples:'))
print("Enter the range")
mn = int(input('Lower Range:'))
mx = int(input('Upper Range:'))
if mn == mx:
    print('It is not a range')
else:
    apple(n,mn,mx)