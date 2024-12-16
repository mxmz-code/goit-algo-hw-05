import logging

def binary_search(arr, target):
    """
    Реалізація двійкового пошуку для відсортованого масиву з дробовими числами.
    Повертає кортеж: (кількість ітерацій, верхня межа - найменший елемент, що більший або рівний заданому значенню)
    """
    # Перевірка на типи даних
    if not isinstance(arr, list):
        raise TypeError("Масив повинен бути списком.")
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Масив повинен містити тільки числа.")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Шуканий елемент повинен бути числом.")
    
    # Перевірка на порожній масив
    if len(arr) == 0:
        logging.warning("Масив порожній. Пошук неможливий.")
        return 0, "Масив порожній"

    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            logging.info(f"Знайдено елемент {target} на індексі {mid} за {iterations} ітерацій.")
            return iterations, arr[mid]  # Елемент знайдений, повертаємо його як верхню межу

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        # Запам'ятовуємо верхню межу (найменший елемент, який більший або рівний target)
        if arr[mid] >= target:
            upper_bound = arr[mid]

    logging.info(f"Елемент {target} не знайдено після {iterations} ітерацій.")
    return iterations, upper_bound if upper_bound is not None else "не знайдено"

def run_task_2():
    """
    Функція для виконання завдання 2:
    Реалізація двійкового пошуку для відсортованого масиву з дробовими числами.
    """
    # Відсортований масив з дробовими числами для тестування
    sorted_array = [0.5, 1.3, 2.7, 3.1, 4.6, 5.8, 7.2, 9.0, 10.1]

    # Тестування: шукаємо існуючий елемент
    target = 5.0
    print(f"Шукаємо елемент {target} в масиві: {sorted_array}")
    iterations, result = binary_search(sorted_array, target)
    if result != "не знайдено":
        print(f"Елемент {target} знайдено на індексі {result}. Кількість ітерацій: {iterations}.")
    else:
        print(f"Елемент {target} не знайдено після {iterations} ітерацій.")
    
    # Тестування: шукаємо неіснуючий елемент
    target = 6.0
    print(f"\nШукаємо елемент {target} в масиві: {sorted_array}")
    iterations, result = binary_search(sorted_array, target)
    if result != "не знайдено":
        print(f"Елемент {target} знайдено на індексі {result}. Кількість ітерацій: {iterations}.")
    else:
        print(f"Елемент {target} не знайдено після {iterations} ітерацій.")

    # Тестування: шукаємо елемент, який не має верхньої межі в масиві
    target = 11.0
    print(f"\nШукаємо елемент {target} в масиві: {sorted_array}")
    iterations, result = binary_search(sorted_array, target)
    if result != "не знайдено":
        print(f"Елемент {target} знайдено на індексі {result}. Кількість ітерацій: {iterations}.")
    else:
        print(f"Елемент {target} не знайдено після {iterations} ітерацій. Верхня межа: {result}")

    return {
        "status": "Завдання 2 виконано успішно.",
        "iterations": iterations,
        "upper_bound": result
    }
