"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def number_predict(number:int=1) -> int:
    """Угадываем число, используя среднее арифметическое 
       концов интервала и уменьшение интервала в 2 раза
       при каждой следующей попытке

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    cur_min = 1
    cur_max = 101

    while True:  
        count += 1
        # Каждая попытка уменьшает интервал для выбора числа в 2 раза
        predict = int((cur_min+cur_max) / 2)

        if predict > number:
            cur_max = predict

        elif predict < number:
            cur_min = predict+1

        else:
            # Выходим при угадывании
            break
    return count


def score_game(number_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов
       угадывает наш алгоритм

    Args:
        number_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    # Загадываем список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(number_predict(number))

    # Находим среднее количество попыток
    score = int(np.mean(count_ls))
    
    print("Ваш алгоритм угадывает число в среднем за:",
          f"{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(number_predict)