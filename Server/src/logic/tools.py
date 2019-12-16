from random import randint


def random_answer(answers, key=None):
    if type(answers) is dict:
        if key is not None:
            index = randint(0, len(answers[key]) - 1)
            return answers[key][index]
    elif type(answers) is list:
        index = randint(0, len(answers) - 1)
        return answers[index]