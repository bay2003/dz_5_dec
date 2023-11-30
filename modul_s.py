# Работа с файлами, удаление создание и т.д.
#
# import os
#
# # Получаем текущую рабочую директорию
# print(os.getcwd())
#
# # Выводим список файлов и папок в текущей рабочей директории
# print(os.listdir())
#
# # Проверяем, существует ли папка 'new0', и удаляем ее, если она существует
# for i in range(1):
#     if not os.path.exists(f'new{i}'):
#         os.mkdir(f'new{i}')
#
# for i in range(1):
#     os.rmdir(f'new{i}')
#
# # Создаем путь к файлу
# path = os.path.join(os.getcwd(), 'main', 'other', 'file.txt')
# print(path)
import sys

# Копирование файлов

# import shutil
#
# shutil.copy('work.py', 'work_copy')

# print(sys.platform)
# Пути где питон ищет файлы
# print(sys.path)

# запуск кода из файла
# sys.path.append("F:GITHUB 1023/dz_5_dec/work.py")
# import work

import random
import math
import functools
import glob

