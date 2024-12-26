from funcs import show_menu
from funcs import execute_algorithm
import threading

def main():
    """
    Основная функция для запуска программы.
    """
    # Создаем поток для отображения меню
    menu_thread = threading.Thread(target=show_menu)
    menu_thread.start()

    # Создаем поток для выполнения расчетов
    calculation_thread = threading.Thread(target=execute_algorithm)
    calculation_thread.start()

    # Ждем завершения потоков
    menu_thread.join()
    calculation_thread.join()

if __name__ == "__main__":
    main()
