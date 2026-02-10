print("Welcome to the rollercoaster!")
height = float(input("What is ur height in cm? "))

if height >= 120:
    print("Can ride!")
    age = int(input("How old are u?"))
    if age < 12:
        print("U should pay $5!")
    elif age >= 12 and age <= 18:
        print("U should pay $7!")
    else:
        print("U shold pay $12!")        
else:
    print("Can't ride!")