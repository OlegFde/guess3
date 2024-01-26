import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict = np.random.randint(1, 101)             # Выбирается случайное число

        if number > predict:
            # Создаётся список случайных чисел размером, скажем, 7, нижняя граница predict
            predict_numbers = np.random.randint(predict, 101, 7)  
        elif number < predict:
            # Создаётся список случайных чисел с тем же размером, верхняя граница predict + 1
            predict_numbers = np.random.randint(1, predict + 1, 7)  
        else:                                           # Число угадано
            break

        ex = False                                      # Флаг для выходя из цикла while
        if number in predict_numbers:                   # Если угадываемое число содержится в диапазоне случайных чисел
            for num in predict_numbers:                 # Осуществляется сравнение каждого числа из диапазона с загаданным
                if number == num:
                    # При нахождении числа производится выход из цикла for с одновременной установкой флага для выхода из цикла while
                    ex = True             
                    break                               
                else:
                    count += 1                          # При каждом несовпадении счётчик увеличивается
            if ex:                                      # Если флаг выхода из while установлен, осуществляется выход
                break
            
    return count

print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)