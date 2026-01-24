score = 0
while True:
    select = int(input("1. Start quiz\n2. Exit\n"))
    if (select == 1):
        questions = [
            {"q": "Q1. What is 2+2?",
             "options": "1. 3\n2. 4\n3. 5\n4. 8",
             "ans": 2},
            {"q": "Q2. 4+4?",
             "options": "1. 5\n2. 8\n3. 9\n4. 10",
             "ans": 2},
            {"q": "Q3. Python is a?",
             "options": "1. Snake\n2. Language\n3. Both\n4. none",
             "ans": 3},
            {"q": "Q4. 5*5?", "options":
             "1. 20\n2. 25\n3. 30\n4. 50",
             "ans": 2},
            {"q": "Q5. 3+3", "options":
             "1. 8\n2. 9\n3. 7\n4. 6",
             "ans": 4}
        ]
        for q in questions:
            print(q["q"])
            print(q["options"])
            ans = int(input("Your answer: "))
            if ans == q["ans"]:
                score += 1
        print("Your score: ", score," out of 5")
        break
    elif select == 2:
        break
    else:
        print("Invalid choice")