import csv
import random


class Quiz:
    """
    check_answer: checks the users input and set point of question

    """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.point = 0

    def check_answer(self, user_answer):
        if self.answer == str(user_answer).capitalize().strip():
            self.point = 10
        if user_answer == '':
            self.point = 0
        elif self.answer != str(user_answer).capitalize().strip():
            self.point = -3
        return self.point

    def __str__(self):
        return f"{self.question}"


class TrueFalse(Quiz):
    """

    check_answer: checks the users input and set score

    """
    pass


class ShortAnswer(Quiz):
    """

    check_answer: checks the users input and set score

    """
    pass


class MultiChoice(Quiz):
    """

    check_answer: checks the users input and set score

    """
    pass


class Score:
    """
    This is a class which the objects relate to users
    self.score=point (which for each user is 0 at first)
    self.category=category (which will set by final score )
    def set_category: staticmethod,tell if the user win or not

    """

    def __init__(self, point):
        self.score = point
        self.category = None

    def set_category(self):
        if self.score >= 40:
            self.category = 'Winner'
        else:
            self.category = 'Your score is less than 40'
        return self.category

    def __add__(self, other):  # reride __add__
        self.score = self.score + other.score
        return Score(self.score)

    def __str__(self):
        return f"{self.score}"


def reading():  # reads file and return a list of sorted by main titels list
    total = {'TrueFalse': [], 'ShortAnswer': [], 'Multiple Choice': []}
    with open('data.csv', 'r') as x:
        x = csv.DictReader(x)
        for row in x:
            total['TrueFalse'].append([row['TrueFalse Question'], row['TrueFalse Answers']])
            total['ShortAnswer'].append([row['ShortAnswer Question'], row['ShortAnswer Answers']])
            total['Multiple Choice'].append([row['Multiple Choice Question'], row['Multiple Choice Answers']])
    return total


def making_object(qtype):  # return a list sampel out of reading return by titel like 'TrueFalse'
    total = reading()
    objectt = random.choice(total[qtype])
    return objectt


# # # # # # # # # # # # # # # # # # # #Run# # # # # # # # # # # # # # # # #


questions = []  # We must have one from all typs of questions
test = making_object('TrueFalse')
questions.append(TrueFalse(test[0], test[1]))
test = making_object('ShortAnswer')
questions.append(ShortAnswer(test[0], test[1]))
test = making_object('Multiple Choice')
questions.append(MultiChoice(test[0], test[1]))

# here we make other 2 random questions
random_select = ['TrueFalse', 'ShortAnswer', 'Multiple Choice']
for i in range(2):
    select = random.choice(random_select)
    x = making_object(select)
    test = Quiz(x[0], x[1])
    for j in questions:  # check for uniqe
        if test.question == j.question:
            select = random.choice(random_select)
            x = making_object(select)
            test = Quiz(x[0], x[1])
        else:
            pass
    questions.append(test)

# #here we make a file for user
y = open('user_test.txt', 'w')
for i, q in enumerate(questions):
    y.write(f"line {i + 1} Q : {q}\n")
    y.write(f"line {i + 1} A : the correct answer is {q.answer}\n")
y.close()

user_score = Score(0)  # Score make an object which is related to user
count_correct, count_wrong = 0, 0  # for display
for i, j in enumerate(questions):
    print(f"Question No{i + 1} : {j}")
    user_answer = input('>>>> ')
    j.check_answer(user_answer)
    if j.point == 10:
        print('Correct Answer!')
        count_correct += 1
    if j.point == -3:
        print('Wrong Answer!')
        count_wrong += 1
    user_score.__add__(Score(j.point))
    print(
        f"Q:{i + 1} Correct:{count_correct} Wrong:{count_wrong} Score:{user_score.score} Remaining:{5 - (i + 1)} \n")

user_score.set_category()
print(user_score.category)
