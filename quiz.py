questions = (
    "Who is the developer of Python?",
    "Which year was Python introduced?",
    "Which is not a data type in Python?",
    "How to denote a variable in Python?",
    "Which operator has higher precedence?"
)
options = (
    ("A. Dennis Ritchie", "B. James Gosling", "C. Guido Van Rossum", "D. Ken Thompson"),
    ("A. 1991", "B. 1992", "C. 1995", "D. 1997"),
    ("A. array", "B. list", "C. string", "D. float"),
    ("A. _a", "B. a_", "C. 0_a", "D. 0"),
    ("A. 5", "B. 9", "C. 7", "D. 2")
)
answers = ("C", "A", "A", "B", "D")
guesses = []
score = 0

for question_num, question in enumerate(questions):
    print("____________________________________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

print(f"\nYour final score is {score}/{len(questions)}")
