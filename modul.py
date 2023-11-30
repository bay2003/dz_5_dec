# modul.py
import random

def get_people_and_quest():
    Test_quest = {
        'Какой сегодня год': 2023, 
        "Как дела на марсе": 20, 
        "зачем такие тупые вопросы": 15
    }
    return random.choice(list(Test_quest.items()))

def run_quiz():
    rounds = int(input('Сколько раз? '))

    for i in range(rounds):
        name, date = get_people_and_quest()
        answer = input(f'Итак вопрос: {name}? ')

        if answer == str(date):
            print('Верно')
        else:
            print('Неверно')
