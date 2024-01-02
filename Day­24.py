#DAY 24 - Introduction to tuples
tup = (("Abhinav", "@NoobieAbhinav"), ("Jayesh", "@ThatCyberNerd"), ("Tanishq", "@ItsMeTanishq"),\
       ("Arnav, @Cricket_Arnav"), ("Joshua", "@CreeCoder"), ("Harsh", "@91chepauk"))
name = input("Enter the name whose Twitter ID you want to find: ")
the_bois = []
for details in tup:
    if details[0].lower() == name.lower():
        print("The given person's Twitter ID is:", details[1])
    the_bois.append(details[0])
if name.capitalize() not in the_bois:
    print("Person not found in our contact book.")