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
