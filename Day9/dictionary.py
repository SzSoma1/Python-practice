programming_dict = {
    "Bug": "An error.",
    "Function": "U can call it over and over again.",
}

empty_dict = {}

programming_dict["Loop"] = "The action of doing smth over and over again."
print(programming_dict["Loop"])

for key in programming_dict:
    print(key)
    print(programming_dict[key])