questions=(("who is a developer of python"),
          ("which is year python is introduce"),
          ("which is not a data type in python"),
          ("how to denote variable in python"),
          ("which operator has higher presidency"),
          ("how many classifications of operator"))
options=(("A. Dennis Ritchi","B. James Gogling","C. Guiod Van Rossum","D. Ken Thompson"),
        ("A. 1991","B. 1992","C. 1995","D. 1997"),
        ("A. array","B. list","C. string","D. float"),
        ("A. _a","B. a_","C. 0_a","D. 0"),
        ("A. 5","B. 9","C. 7","D. 2"))
answers=("C","A","A","B","D")
guesses=[]
score=0
question_num=0
for question in questions:
    print("____________________________________________")
    print(question)
    for option in options[question_num]:
        print(option)

        guess=input("Enter(A,B,C,D):").upper()
        guesses.append(guess)
        if guess ==answers[question_num]:
            print("CORRECT")
            score+=1
        else:
            print("INCORRECT")
            print("f{answers[question_num]}is correct answer")
        question_num+=1