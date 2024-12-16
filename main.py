import os
import logging
from tasks.task_1 import run_task_1
from tasks.task_2 import run_task_2
from tasks.task_3 import run_task_for_random_file

# Налаштування логування з збереженням в папці logs
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'program_log.txt'), level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def clear_screen():
    """Очищає екран. Працює на всіх операційних системах."""
    os.system("cls" if os.name == "nt" else "clear")

def print_menu():
    """Виводить головне меню програми."""
    print("===================================")
    print("           Головне меню            ")
    print("===================================")
    print("1. Завдання 1: Видалення пари ключ-значення у таблиці HashTable.")
    print("2. Завдання 2: Реалізація двійкового пошуку для відсортованого масиву.")
    print("3. Завдання 3: Порівняння ефективності алгоритмів пошуку підрядка.")
    print("0. Вихід")
    print("===================================")

def get_user_choice():
    """Отримує вибір користувача та перевіряє його коректність."""
    while True:
        try:
            choice = int(input("Оберіть варіант (1-3) або натисніть 0 для виходу: "))
            if choice in [0, 1, 2, 3]:
                return choice
            else:
                print("Невірний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть правильне число.")

def clear_and_print_menu():
    """Очищає екран і виводить меню."""
    clear_screen()
    print_menu()

def main():
    """Основна функція програми."""
    while True:
        clear_and_print_menu()
        choice = get_user_choice()
        
        results = {}
        
        if choice == 1:
            print("\nЗапуск Завдання 1: Видалення пари ключ-значення у таблиці HashTable.")
            task_1_result = run_task_1()  # Ваш код для завдання 1
            results["task_1"] = {
                "status": "Завдання 1 виконано успішно.",
                "data": task_1_result  # Результати виконання завдання 1
            }
            logging.info(f"Результат Завдання 1: {results['task_1']}")
            print("Завдання 1 виконано успішно!")
        elif choice == 2:
            print("\nЗапуск Завдання 2: Реалізація двійкового пошуку для відсортованого масиву.")
            task_2_result = run_task_2()  # Ваш код для завдання 2
            results["task_2"] = {
                "status": "Завдання 2 виконано успішно.",
                "data": task_2_result  # Результати виконання завдання 2
            }
            logging.info(f"Результат Завдання 2: {results['task_2']}")
            print("Завдання 2 виконано успішно!")
        elif choice == 3:
            print("\nЗапуск Завдання 3: Порівняння ефективності алгоритмів пошуку підрядка.")
            task_3_result = run_task_for_random_file()  # Ваш код для завдання 3
            results["task_3"] = {
                "status": "Завдання 3 виконано успішно.",
                "data": task_3_result  # Результати виконання завдання 3
            }
            logging.info(f"Результат Завдання 3: {results['task_3']}")
            print("Завдання 3 виконано успішно!")
        elif choice == 0:
            print("\nВихід з програми...")
            logging.info("Програма завершена.")
            break
        else:
            print("\nНевірний вибір. Спробуйте ще раз.")

        # Виведення результатів у лог, можна також додати додаткову обробку
        input("\nНатисніть Enter для продовження...")
        clear_screen()  # Очищення екрану перед наступним циклом

if __name__ == "__main__":
    main()
