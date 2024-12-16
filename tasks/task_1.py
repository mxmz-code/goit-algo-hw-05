import logging

class HashTable:
    def __init__(self, size=10):
        """
        Ініціалізація хеш-таблиці з визначеним розміром.
        """
        self.size = size
        self.table = [None] * size
        logging.info(f"Створено хеш-таблицю з розміром {size}.")

    def hash_function(self, key):
        """
        Функція для генерування хешу для ключа.
        Використовуємо простий алгоритм хешування.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Вставка пари ключ-значення в хеш-таблицю.
        """
        try:
            index = self.hash_function(key)
            if self.table[index] is None:
                self.table[index] = [(key, value)]
            else:
                self.table[index].append((key, value))
            logging.info(f"Вставлено: ({key}, {value})")
        except Exception as e:
            logging.error(f"Помилка при вставці: {e}")
            print(f"Помилка при вставці елемента: {e}")

    def delete(self, key):
        """
        Видалення пари ключ-значення з хеш-таблиці.
        Якщо ключ не знайдено, вивести повідомлення про помилку.
        """
        try:
            index = self.hash_function(key)
            if self.table[index] is None:
                logging.warning(f"Ключ {key} не знайдено для видалення.")
                return f"Ключ {key} не знайдено в таблиці."
            
            for i, (stored_key, stored_value) in enumerate(self.table[index]):
                if stored_key == key:
                    del self.table[index][i]
                    logging.info(f"Видалено: ({key}, {stored_value})")
                    return f"Ключ {key} успішно видалено."
            
            logging.warning(f"Ключ {key} не знайдено для видалення.")
            return f"Ключ {key} не знайдено в таблиці."
        except Exception as e:
            logging.error(f"Помилка при видаленні: {e}")
            print(f"Помилка при видаленні елемента: {e}")

    def display(self):
        """
        Виведення всіх елементів хеш-таблиці для перегляду її вмісту.
        """
        try:
            for i, item in enumerate(self.table):
                if item is not None:
                    print(f"Індекс {i}: {item}")
                else:
                    print(f"Індекс {i}: Порожньо")
        except Exception as e:
            logging.error(f"Помилка при відображенні таблиці: {e}")
            print(f"Помилка при відображенні таблиці: {e}")

def run_task_1():
    """
    Функція для виконання завдання 1.
    Створення хеш-таблиці, вставка та видалення елементів.
    """
    # Створюємо хеш-таблицю
    hash_table = HashTable()

    # Вставка кількох елементів
    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("cherry", 30)

    # Виведення таблиці перед видаленням
    print("До видалення:")
    hash_table.display()

    # Видалення елемента
    result = hash_table.delete("banana")
    print(result)  # Виведення результату видалення
    
    # Виведення таблиці після видалення
    print("Після видалення:")
    hash_table.display()

    return "Завдання 1 виконано успішно."
