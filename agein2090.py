def converter(age):
    if age < 1000:
        age = 2024 - age
    return age

def Yourage(age, yrs = 0):
    year = converter(age)
    print(f"Your age in 2090 is {2090 -year}")
    print(f"You are 100 years old in {year + 100}")

    if yrs != 0:
        print(f"Your age in {yrs} is {yrs - year}")


age = int(input("Enter your age or birth year"))
yrs = 0
print("Do you age to enter the year to find age")
choice = str.upper(input("Y/N"))
if choice == "Y":
    yrs = int(input("Enter the year"))
    yrr = yrs

else: 
    yrr = 2024

try:
    Yourage(age,yrs)

    if age > 150 and age < 1900 :
        raise ValueError("I think you are oldest person in the planet")

    elif age < 0 or age >2024:
        raise ValueError("I even born yet")

    elif yrr < age:
        raise ValueError("Invalid Year")

except ValueError as e:
    print(e)


    

    
