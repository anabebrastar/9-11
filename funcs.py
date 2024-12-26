import random

# Глобальные переменные для хранения состояния программы
selected_task = None
matrix = None
array1 = None
array2 = None
array = None
target_sum = None
result = None

# Функция для отображения главного меню
def show_menu():
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

# Функция для выбора задания
def select_task():
    print("Выберите задание:")
    print("1. Поворот матрицы")
    print("2. Сумма или разность больших чисел")
    print("3. Подмассивы с заданной суммой")
    global selected_task
    selected_task = input("Введите номер задания: ")

# Функция для ввода данных в зависимости от выбранного задания
def input_data():
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

# Функция для ввода матрицы
def input_matrix():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Введите {m} элементов для строки {i+1}: ").split()))
        matrix.append(row)
    return matrix

# Функция для ввода двух больших чисел
def input_large_numbers():
    array1 = list(map(int, input("Введите первое большое число: ").split()))
    array2 = list(map(int, input("Введите второе большое число: ").split()))
    return array1, array2

# Функция для ввода массива и числа
def input_array_and_sum():
    array = list(map(int, input("Введите массив: ").split()))
    target_sum = int(input("Введите число: "))
    return array, target_sum

# Функция для генерации случайной матрицы
def generate_random_matrix(n, m):
    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

# Функция для генерации случайных больших чисел
def generate_random_large_numbers(length):
    return [random.randint(0, 9) for _ in range(length)]

# Функция для генерации случайного массива
def generate_random_array(length):
    return [random.randint(0, 9) for _ in range(length)]

# Функция для выполнения алгоритма в зависимости от выбранного задания
def execute_algorithm():
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

# Функция для поворота матрицы
def rotate_matrix(matrix, direction):
    if direction == 'clockwise':
        return [list(row) for row in zip(*matrix[::-1])]
    elif direction == 'counterclockwise':
        return [list(row) for row in zip(*matrix)][::-1]
    else:
        raise ValueError("Неверное направление поворота")

# Функция для суммы или разности больших чисел
def sum_large_numbers(array1, array2, operation):
    if operation == 'sum':
        return [a + b for a, b in zip(array1, array2)]
    elif operation == 'difference':
        return [a - b for a, b in zip(array1, array2)]
    else:
        raise ValueError("Неверная операция")

# Функция для подсчета подмассивов с заданной суммой
def count_subarrays_with_sum(array, target_sum):
    count = 0
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum == target_sum:
                count += 1
    return count

# Функция для вывода результата
def output_result():
    if result is not None:
        print("Результат:")
        print(result)
    else:
        print("Сначала выполните алгоритм.")
