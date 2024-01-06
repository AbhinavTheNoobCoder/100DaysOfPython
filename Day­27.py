#DAY 27 - Kaun Banega Crorepati / Who Wants To Be a Millionaire
print('''Welcome to Kaun Banega Crorepati.
You will be asked 10 questions. Kindly reply with the A, B, C or D.''')
q1 = '''For Rs 1000:
Which of the following is a natural satellite of Earth?
a) Mars
b) Venus
c) Moon
d) Jupiter'''
q2 = '''For Rs 2000
What is the capital city of Australia?
a) Sydney
b) Melbourne
c) Canberra
d) Brisbane'''
q3 = '''For Rs 3000:
In the context of computers, what does the acronym 'RAM' stand for?
a) Random Access Memory
b) Read-Only Memory
c) Remote Access Module
d) Real-time Audio Module'''
q4 = '''For Rs 5000:
Which famous scientist developed the theory of relativity?
a) Isaac Newton
b) Albert Einstein
c) Galileo Galilei
d) Stephen Hawking'''
q5 = '''For Rs 10000:
What is the largest mammal in the world?
a) Elephant
b) Blue Whale
c) Giraffe
d) Gorilla'''
q6 = '''For Rs 20000:
In which year did India gain independence from British rule?
a) 1942
b) 1947
c) 1950
d) 1962'''
q7 = '''For Rs 40000:
Who is the author of the Harry Potter book series?
a) J.R.R. Tolkien
b) J.K. Rowling
c) George R.R. Martin
d) Suzanne Collins'''
q8 = '''For Rs 80000:
Who wrote the play "Romeo and Juliet"?
a) William Shakespeare
b) Charles Dickens
c) Jane Austen
d) Mark Twain'''
q9 = '''For Rs 160000:
Which planet is known as the "Red Planet"?
a) Venus
b) Mars
c) Jupiter
d) Saturn'''
q10 = '''For Rs 320000 - Maximum Price:
What is the currency of Japan?
a) Won
b) Yen
c) Baht
d) Ringgit'''
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
answers = ["c","c","a","b","b","b","b","a","b","b"]
prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
count = 0
for i in questions:
    ask = input(i + "\n")
    if ask.lower() == answers[count]:
        print("Correct.")
        print()
        count += 1
        continue
    else:
        print("Unfortunately, that's wrong and you have lost.")
        print("The correct answer was", answers[count])
        break
print("You have won Rs", prizes[count-1])