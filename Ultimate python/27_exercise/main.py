
questions = [
    ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "PHP", "None", 4],
    ["Who is the founder of Microsoft?", "Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Elon Musk", "None", 2],
    ["Which language is used for Android app development?", "Java", "HTML", "CSS", "PHP", "None", 1],
    ["What does HTML stand for?", "Hyper Text Markup Language", "High Text Machine Language", "Hyper Transfer Markup Language", "Home Tool Markup Language", "None", 1],
    ["Which company developed Python?", "Microsoft", "Google", "Python Software Foundation", "Apple", "None", 3],
    ["Which symbol is used for comments in Python?", "//", "#", "/* */", "<!-- -->", "None", 2],
    ["Which of the following is a database?", "HTML", "CSS", "MySQL", "JavaScript", "None", 3],
    ["Who created the C programming language?", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum", "None", 2],
    ["Which company developed Java?", "Sun Microsystems", "Google", "Apple", "IBM", "None", 1],
    ["What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User", "None", 1],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    print(f"e. {question[5]}")
    reply = int(input("Enter your answer (1-5) or 0 to quit: "))
    if reply == 0:
        print("You quit the game!")
        break
    if reply == question[-1]:
        print(f"Correct answer! You have won Rs. {levels[i]}")
        money = levels[i]
    else:
        print("Wrong answer!")
        break
print(f"\nYour take-home money is Rs. {money}")
