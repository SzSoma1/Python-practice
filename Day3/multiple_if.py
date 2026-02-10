print("Welcome to the rollercoaster!")
height = float(input("What is ur height in cm? "))
bill = 0

if height >= 120:
    print("Can ride!")
    age = int(input("How old are u?"))
    if age < 12:
        print("Child should pay $5!")
        bill = 5
    elif age >= 12 and age <= 18:
        print("Youth should pay $7!")
        bill = 7    
    elif 45 <= age <= 55:
        print("U will get a free ride!")   
    else:
        print("Adult shold pay $12!")
        bill = 12  
    wants_photo = input("Do u need the photo? Type y or n!")   
    if wants_photo == "y":
        bill += 3        
    print(f"U should pay ${bill}")      
else:
    print("Can't ride!")