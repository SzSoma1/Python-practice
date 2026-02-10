print("Welcome to the pizza deliveries!")
size = input("What size do u want? S, M or L?")
pepperoni = input("Do u want pepperoni on it? Y or N?")
extra_cheese = input("Do u want extra cheese on it? Y or N?")
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill +=2
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("U choose wrong inputs!")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3    
    
if extra_cheese == "Y":
    bill += 1

print(f"U should pay ${bill} for ur pizza!")            