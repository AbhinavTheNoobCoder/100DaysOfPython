#DAY 30 - Introduction to Sets
set1 = {"EA", "Sports", "It's", "In", "The", "Game"}
set2 = {"Chipi", "Chipi", "Chapa", "Chapa"} #no duplicates considered
print(set1)
print(set2)
emptyset = set()
set3 = {"Mumbai", "Delhi", "Hyderabad", "Chennai", "Kolkata"}
set4 = {"Bangalore", "Hyderabad", "Delhi", "Roorkee", "Guwahati"}
print("Set 3", set3)
print("Set 4", set4)
intersection = []
for i in set3:
    if i in set4:
        intersection.append(i)
intersection = set(intersection)
print("Intersection of set3 and set4 is", intersection)