#DAY 16 - match-case statements
x = int(input("Enter your age in years: "))
match x:
    case _ if x < 18:
        print("You're not an adult yet.")
    case 18:
        print("Just turned into an adult, huh?")
    case _:
        print("You're an adult.")
        match x:
            case _ if x < 21:
                print("You cannot drink liquor yet.")
            case _:
                print("You can drink liquor legally.")