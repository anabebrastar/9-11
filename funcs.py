import random

# Глобальные переменные для хранения состояния программы
selected_task = None
matrix = None
array1 = None
array2 = None
array = None
target_sum = None
result = None

def show_menu():
    """
    Отображает главное меню и обрабатывает выбор пользователя.
    """
    while True:
        print("Меню:")
        print("1. Выбор задания")
        print("2. Ввод исходных данных")
        print("3. Выполнение алгоритма по заданию")
        print("4. Вывод результата")
        print("5. Завершение работы программы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            select_task()
        elif choice == '2':
            input_data()
        elif choice == '3':
            execute_algorithm()
        elif choice == '4':
            output_result()
        elif choice == '5':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def select_task():
    """
    Позволяет пользователю выбрать задание.
    """
    print("Выберите задание:")
    print("1. Поворот матрицы")
    print("2. Сумма или разность больших чисел")
    print("3. Подмассивы с заданной суммой")
    global selected_task
    selected_task = input("Введите номер задания: ")

def input_data():
    """
    В зависимости от выбранного задания, вызывает соответствующую функцию для ввода данных.
    """
    global matrix, array1, array2, array, target_sum, result
    result = None
    if selected_task == '1':
        print("Выберите способ ввода данных:")
        print("1. Ручной ввод")
        print("2. Случайная генерация")
        choice = input("Выберите способ ввода данных: ")
        if choice == '1':
            matrix = input_matrix()
        elif choice == '2':
            n = int(input("Введите количество строк матрицы: "))
            m = int(input("Введите количество столбцов матрицы: "))
            matrix = generate_random_matrix(n, m)
            print("Сгенерированная матрица:")
            for row in matrix:
                print(row)
        else:
            print("Неверный выбор. Попробуйте снова.")
    elif selected_task == '2':
        print("Выберите способ ввода данных:")
        print("1. Ручной ввод")
        print("2. Случайная генерация")
        choice = input("Выберите способ ввода данных: ")
        if choice == '1':
            array1, array2 = input_large_numbers()
        elif choice == '2':
            length = int(input("Введите длину больших чисел: "))
            array1 = generate_random_large_numbers(length)
            array2 = generate_random_large_numbers(length)
            print("Сгенерированные большие числа:")
            print("Число 1:", array1)
            print("Число 2:", array2)
        else:
            print("Неверный выбор. Попробуйте снова.")
    elif selected_task == '3':
        print("Выберите способ ввода данных:")
        print("1. Ручной ввод")
        print("2. Случайная генерация")
        choice = input("Выберите способ ввода данных: ")
        if choice == '1':
            array, target_sum = input_array_and_sum()
        elif choice == '2':
            length = int(input("Введите длину массива: "))
            array = generate_random_array(length)
            target_sum = int(input("Введите число: "))
            print("Сгенерированный массив:", array)
        else:
            print("Неверный выбор. Попробуйте снова.")
    else:
        print("Сначала выберите задание.")

def input_matrix():
    """
    Позволяет пользователю ввести матрицу.
    """
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Введите {m} элементов для строки {i+1}: ").split()))
        matrix.append(row)
    return matrix

def input_large_numbers():
    """
    Позволяет пользователю ввести два больших числа.
    """
    array1 = list(map(int, input("Введите первое большое число: ").split()))
    array2 = list(map(int, input("Введите второе большое число: ").split()))
    return array1, array2

def input_array_and_sum():
    """
    Позволяет пользователю ввести массив и число.
    """
    array = list(map(int, input("Введите массив: ").split()))
    target_sum = int(input("Введите число: "))
    return array, target_sum

def generate_random_matrix(n, m):
    """
    Генерирует случайную матрицу размером n x m.
    """
    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

def generate_random_large_numbers(length):
    """
    Генерирует случайные большие числа длиной length.
    """
    return [random.randint(0, 9) for _ in range(length)]

def generate_random_array(length):
    """
    Генерирует случайный массив длиной length.
    """
    return [random.randint(0, 9) for _ in range(length)]

def execute_algorithm():
    """
    Выполняет алгоритм в зависимости от выбранного задания.
    """
    global result
    if selected_task == '1':
        direction = input("Введите направление поворота (clockwise/counterclockwise): ")
        result = rotate_matrix(matrix, direction)
    elif selected_task == '2':
        operation = input("Введите операцию (sum/difference): ")
        result = sum_large_numbers(array1, array2, operation)
    elif selected_task == '3':
        result = count_subarrays_with_sum(array, target_sum)
    else:
        print("Сначала выберите задание и введите данные.")

def rotate_matrix(matrix, direction):
    """
    Поворачивает матрицу на 90 градусов по часовой стрелке или против часовой стрелки.
    """
    if direction == 'clockwise':
        return [list(row) for row in zip(*matrix[::-1])]
    elif direction == 'counterclockwise':
        return [list(row) for row in zip(*matrix)][::-1]
    else:
        raise ValueError("Неверное направление поворота")

def sum_large_numbers(array1, array2, operation):
    """
    Выполняет сумму или разность двух больших чисел.
    """
    if operation == 'sum':
        return [a + b for a, b in zip(array1, array2)]
    elif operation == 'difference':
        return [a - b for a, b in zip(array1, array2)]
    else:
        raise ValueError("Неверная операция")

def count_subarrays_with_sum(array, target_sum):
    """
    Подсчитывает количество подмассивов, сумма которых равна заданному числу.
    """
    count = 0
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum == target_sum:
                count += 1
    return count

def output_result():
    """
    Выводит результат выполнения алгоритма.
    """
    if result is not None:
        print("Результат:")
        print(result)
    else:
        print("Сначала выполните алгоритм.")
