"""Game Guess the number
   The computer itself makes a guess and guesses the number  
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """randomly guess the number

    Args:
        number (int, optional): The hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0    
    min = 1 # устанавливаем минимальное и максимальное значение предполагаемого числа
    max = 101
    
    while True:
        count += 1
        predict_number = np.random.randint(min, max) # предполагаемое число
        if predict_number > number: 
            max = predict_number  # изменяем максимальное число для поиска
        elif predict_number < number:
            min = predict_number  # изменяем минимальное число для поиска
        else:
            break # угадали число, выходим из цикла
    return(count)



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел и определили число повторений

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(random_predict)

