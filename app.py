from question import Question

question_prompts = [
    "What color are Oranges?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Eggplants?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Bananas?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], ""),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('you got ' + str(score) + '/'+ str(len(questions)) + ' correct')

run_test(questions)