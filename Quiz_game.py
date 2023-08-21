import random
run = True
QUESTIONS = ["What is the capital of Brazil?",
             "How many planets is in our solar system?",
             "What language are spoken in India?",
             "When the WW2 was over?"]

ANSWERS = ["brasilia", "8", "hindi", "1945"]

while run:
    take_a_question = random.choices(QUESTIONS)
    print(*take_a_question)
    q_pos = QUESTIONS.index(*take_a_question)
    USER = input(": ").lower()
    print("Is not an answer!")
    a_pos = ANSWERS.index(f"{USER}")

    if a_pos == q_pos:
        print("Correct")
    else:
        print("Incorrect")

    play = input("Do you want another question?(yes/no)").lower()
    if play == "yes":
        continue
    else:
        run = False
        print("Ok Bye!")




