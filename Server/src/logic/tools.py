from random import randint


def random_answer(answers, key):
    index = randint(0, len(answers[key]) - 1)
    return answers[key][index]