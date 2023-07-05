import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # global count

    def count_random(number, start = 1, end = 101, count = 0):
        """Перебираем числа

        Args:
            number (int, optional): Искомое число которое необходимо угадать
            start (int, optional): Изначальный старт диапазона рандомных чисел. Defaults to 1.
            end (int, optional): Изначальное окончание диапазона рандомных чисел. Defaults to 101.
            count (int, optional): Количество попыток угадать число. Defaults to 0.

        Returns:
            int: число попыток
        """
        count += 1
        predict_number = np.random.randint(start, end) # предполагаемое число
        # Если предполагаемое число равно заданному, то возвращаем количество попыток
        if number == predict_number:
            return count
        # Если предполагаемое число больше искомого, то снова вызываем функцию с окончанием равным последнему предполагаемому числу
        elif number < predict_number:
            return count_random(number, start, predict_number, count)
        # Если предполагаемое число меньше искомого, то снова вызываем функцию с стартом равным предполагаемому числу
        else:
            return count_random(number, predict_number, end, count)
    
    count = count_random(number)
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
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    # RUN
    score_game(random_predict)