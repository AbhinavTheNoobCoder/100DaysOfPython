# #DAY 40 - Exercise 4 - Secret Code Language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three
# random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end.
# Now remove the last letter and append it to the beginning

import random
ordinals = [[chr(i) for i in range(65, 91)], [chr(i) for i in range(97, 123)]]

def Coding(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) < 3:
            new_words.append(word[: : -1])
        else:
            suffix = prefix = ""
            for i in range(3):
                code_char = random.choice(ordinals)
                letter = random.choice(code_char)
                prefix += letter
            for i in range(3):
                code_char = random.choice(ordinals)
                letter = random.choice(code_char)
                suffix += letter
            word = prefix + word[1:] + word[0] + suffix
            new_words.append(word)
    new_sentence = ' '.join(new_words)
    return new_sentence

def Decoding(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if len(word) < 3:
            new_words.append(word[: : -1])
        else:
            word = word[3: -3]
            word = word[-1] + word[:-1]
            new_words.append(word)
    new_sentence = ' '.join(new_words)
    return new_sentence

users_sentence = input("Enter a sentence for coding or decoding: ")
x = input("Do you want to code (C) or decode (D) your sentence?: ").lower()
match x:
    case "c":
        print(Coding(users_sentence))
    case "d":
        print(Decoding(users_sentence))
    case _:
        print("Invalid input.")