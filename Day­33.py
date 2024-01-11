#DAY 33 - Introduction to dictionaries
fifa_winners = {"Brazil": 5, "Germany": 4, "Italy": 4, "Argentina": 3, "France": 2, "Uruguay": 2,
"England": 1, "Spain": 1}
country = input("Enter your country: ").capitalize()
print(f"Number of FIFA WCs won by {country} = {fifa_winners.get(country)}")
# fifa_winners[country] works only if country is in the dictionary - throws an error otherwise
print(f"""Here is a list of FIFA WC winners and the number of times they won:
{fifa_winners.items()}""")
#also learnt about dictionary.keys() and dictionary.values()