#DAY 26 - Random code from my side lmao
s = input("Enter a sentence so that we can reverse it: ")
wordlist = s.split()
wordlist.reverse()
reversed = " ".join(wordlist)
print("Original sentence -", s)
print("Reversed sentence -", reversed)