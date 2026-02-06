print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would u like to give? 10, 12, 15\n"))
persons = int(input("How many people to split the bill?\n"))
pay = (total + (total * (tip / 100))) / persons
print(f"Each person should pay:${round(pay, 2)}")
