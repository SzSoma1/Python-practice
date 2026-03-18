capitals = {
    "France": "Paris",
    "Hungary": "Budapest",
    "England": "London",
    
}

travel_log = {
    "Hungary": ["Miskolc", "Budapest"],
}

print(travel_log["Hungary"][1])

nested_list = ["a", "b", ["c", "d"]]
print(nested_list[2][1])

travel_log2 = {
    "France": {
               "num_times_visited": 3,
               "cities_visited": ["Paris", "Dijon"],
               },
}

print(travel_log2["France"]["cities_visited"][1])