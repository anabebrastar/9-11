import random

selected_task = None
matrix = None
array1 = None
array2 = None
array = None
target_sum = None
result = None

def input_data():
    global matrix, array1, array2, array, target_sum, result
    result = None
    if selected_task == '1':
        matrix = input_matrix()
    elif selected_task == '2':
        array1, array2 = input_large_numbers()
    elif selected_task == '3':
        array, target_sum = input_array_and_sum()
    else:
        print("Сначала выберите задание.")

def input_matrix():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Введите {m} элементов для строки {i+1}: ").split()))
        matrix.append(row)
    return matrix
 
def input_large_numbers():
    array1 = list(map(int, input("Введите первое большое число: ").split()))
    array2 = list(map(int, input("Введите второе большое число: ").split()))
    return array1, array2

def input_array_and_sum():
    array = list(map(int, input("Введите массив: ").split()))
    target_sum = int(input("Введите число: "))
    return array, target_sum

def generate_random_matrix(n, m):
    return [[random.randint(0, 9) for _ in range(m)] for _ in range(n)]

def generate_random_large_numbers(length):
    return [random.randint(0, 9) for _ in range(length)]

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

def output_result():
    if result is not None:
        print("Результат:")
        print(result)
    else:
        print("Сначала выполните алгоритм.")



