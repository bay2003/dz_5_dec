#
# import random
#
# Test_quest = {'Какой сегодня год': 2023, "Как дела на марсе": 20, "зачем такие тупые вопросы": 15}
#
# def get_people_and_quest():
#     return random.choice(list(Test_quest.items()))
#
# # Получаем количество раундов
# rounds = int(input('Сколько раз?'))
#
# # Организуем цикл на заданное количество раундов
# for i in range(rounds):
#     # Получаем вопрос и ответ
#     name, date = get_people_and_quest()
#
#     # Задаем вопрос пользователю
#     answer = input(f'Итак вопрос: {name}? ')
#
#     # Проверяем ответ
#     if answer == str(date):  # Приводим date к строке для сравнения
#         print('Верно')
#     else:
#         print('Неверно')

import random

def get_people():
    Test_quest = {'Какой сегодня год': 2023, "Как дела на марсе": 20, "зачем такие тупые вопросы": 15}
    # Случайно выбираем пару вопрос-ответ
    name, date = random.choice(list(Test_quest.items()))
    return name, date

# Получаем вопрос и ответ
name, date = get_people()

# Задаем вопрос
ques = input(f'Вопрос: {name}? ')

# Проверяем ответ
if ques == str(date):
    print('LF')
else:
    print('sa')

print(name, date)



