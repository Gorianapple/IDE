import numpy as np
number = np.random.randint(1, 101)
def game_core_v3(number: int = 1) -> int:
    """Находим загаданное число методом исключения.
       Функция приимает загаданное число и возвращает среднее число попыток. 
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 101
    mid_number = (max_number + min_number) // 2
    
    while mid_number != number:
        count += 1
        if mid_number > number:
            max_number = mid_number  # уменьшаем верхнюю границу
        elif mid_number < number:
            min_number = mid_number  # увеличиваем нижнюю границу
        
        mid_number = (max_number + min_number) // 2
    
    return count
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)