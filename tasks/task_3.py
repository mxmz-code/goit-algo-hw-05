import time
import random
import os
import chardet
import matplotlib.pyplot as plt

# Функция для записи результатов в файл markdown
def save_results_to_markdown(fastest_algorithm, slowest_algorithm, fastest_time, slowest_time, percent_difference, times_existing, times_non_existing):
    """
    Зберігає висновки про швидкість алгоритмів в файл у форматі Markdown.
    """
    markdown_content = f"""
    # Висновки щодо порівняння алгоритмів пошуку підрядка

    ## Найшвидший алгоритм
    Найшвидший алгоритм: **{fastest_algorithm}** з часом **{fastest_time:.6f} секунд**.

    ## Найповільніший алгоритм
    Найповільніший алгоритм: **{slowest_algorithm}** з часом **{slowest_time:.6f} секунд**.

    ## Процентна різниця
    Процентна різниця між найшвидшим та найповільнішим алгоритмом: **{percent_difference:.2f}%**.

    ## Детальні результати для існуючого підрядка:
    """
    for algo, result in times_existing.items():
        markdown_content += f"**{algo}**: Час: **{result['time']:.6f} секунд**, Позиція підрядка: **{result['result']}**\n"

    markdown_content += "\n## Детальні результати для вигаданого підрядка:\n"
    for algo, result in times_non_existing.items():
        markdown_content += f"**{algo}**: Час: **{result['time']:.6f} секунд**, Позиція підрядка: **{result['result']}**\n"

    # Зберігаємо у файл
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    with open(os.path.join(log_dir, 'results_comparison.md'), 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print("\nВисновки збережено у файл results_comparison.md в папці logs.")

def boyer_moore(text, pattern):
    """
    Алгоритм Бойєра-Мура для пошуку підрядка в тексті.
    """
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1
    bad_char = {pattern[i]: i for i in range(m)}
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

def kmp(text, pattern):
    """
    Алгоритм Кнута-Морріса-Пратта для пошуку підрядка в тексті.
    """
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def rabin_karp(text, pattern):
    """
    Алгоритм Рабіна-Карпа для пошуку підрядка в тексті.
    """
    m, n, base, prime = len(pattern), len(text), 256, 101
    pattern_hash, text_hash = 0, 0
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    for i in range(n - m + 1):
        if pattern_hash == text_hash and text[i:i + m] == pattern:
            return i
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * (base ** (m - 1))) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return -1

def compare_algorithms(text, pattern):
    """
    Порівняння часу виконання трьох алгоритмів для пошуку підрядка.
    """
    times = {}
    algorithms = {'Boyer-Moore': boyer_moore, 'KMP': kmp, 'Rabin-Karp': rabin_karp}

    for algorithm_name, algorithm in algorithms.items():
        start_time = time.time()
        result = algorithm(text, pattern)
        elapsed_time = time.time() - start_time
        times[algorithm_name] = {
            'time': elapsed_time,
            'result': result  # додаємо позицію знайденого підрядка або -1
        }
        print(f"{algorithm_name}: Знайдено на позиції {result}, час: {elapsed_time:.6f} секунд")

    fastest_algorithm = min(times, key=lambda x: times[x]['time'])
    slowest_algorithm = max(times, key=lambda x: times[x]['time'])
    fastest_time = times[fastest_algorithm]['time']
    slowest_time = times[slowest_algorithm]['time']
    
    print(f"\nНайшвидший алгоритм: {fastest_algorithm} з часом {fastest_time:.6f} секунд")
    print(f"Найповільніший алгоритм: {slowest_algorithm} з часом {slowest_time:.6f} секунд")

    # Перевірка на нуль перед розрахунком процентної різниці
    if fastest_time > 0:
        percent_difference = ((slowest_time - fastest_time) / fastest_time) * 100
        print(f"Процентна різниця між найшвидшим та найповільнішим алгоритмом: {percent_difference:.2f}%")
    else:
        print("Не можна розрахувати процентну різницю через дуже малий час виконання найшвидшого алгоритму.")

    return times

def visualize_comparison(times_existing, times_non_existing):
    """
    Візуалізація порівняння часу виконання алгоритмів.
    """
    labels = ['Boyer-Moore', 'KMP', 'Rabin-Karp']
    
    # Візуалізація часу для існуючого підрядка
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    ax[0].bar(labels, [times_existing[algo]['time'] for algo in labels], color=['blue', 'green', 'orange'])
    ax[0].set_title('Час для існуючого підрядка')
    ax[0].set_xlabel('Алгоритм')
    ax[0].set_ylabel('Час (секунди)')
    
    # Візуалізація часу для вигаданого підрядка
    ax[1].bar(labels, [times_non_existing[algo]['time'] for algo in labels], color=['blue', 'green', 'orange'])
    ax[1].set_title('Час для вигаданого підрядка')
    ax[1].set_xlabel('Алгоритм')
    ax[1].set_ylabel('Час (секунди)')
    
    plt.tight_layout()
    plt.show()

def select_random_file_from_directory(directory):
    """
    Функція для вибору випадкового текстового файлу з директорії.
    """
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    if not txt_files:
        raise FileNotFoundError("У папці немає текстових файлів.")
    return random.choice(txt_files)

def detect_file_encoding(file_path):
    """
    Функція для визначення кодування файлу.
    Першим пробуємо UTF-8, якщо не вдалося — ISO-8859-1, потім Windows-1251.
    """
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)  # Читаємо перші 10000 байт для визначення кодування
        result = chardet.detect(raw_data)
        return result['encoding']

def run_task_for_random_file():
    """
    Функція для виконання завдання 3: Порівняння ефективності алгоритмів
    пошуку підрядка для випадкового файлу.
    """
    # Це повідомлення тепер виводиться тільки один раз.
    print("Запуск Завдання 3: Порівняння ефективності алгоритмів пошуку підрядка.")
    
    # Вибір випадкового файлу з директорії txt
    try:
        file_name = select_random_file_from_directory('txt')
        file_path = f'txt/{file_name}'
        
        # Визначаємо кодування файлу
        encoding = detect_file_encoding(file_path)
        print(f"Кодування файлу {file_name}: {encoding}")
        
        # Читаємо файл з визначеним кодуванням
        with open(file_path, 'r', encoding=encoding) as file:
            text = file.read()
        
        # Збільшуємо розмір тексту для більш точних обчислень
        text *= 5000  # Умножаємо текст на 5000 для збільшення його розміру
        
    except Exception as e:
        print(f"Помилка при виборі файлу: {e}")
        return
    
    # Випадкові підрядки для пошуку
    existing_pattern = random.choice(text.split())  # Підрядок, що існує в тексті
    non_existing_pattern = "ZZZZZZZZZZZZZZZZ"  # Підрядок, якого точно немає в тексті
    
    print(f"Існуючий підрядок для пошуку: {existing_pattern}")
    print(f"Неіснуючий підрядок для пошуку: {non_existing_pattern}")
    
    # Порівняння алгоритмів для існуючого підрядка
    print("\nТестування для існуючого підрядка:")
    times_existing = compare_algorithms(text, existing_pattern)
    
    # Порівняння алгоритмів для вигаданого підрядка
    print("\nТестування для вигаданого підрядка:")
    times_non_existing = compare_algorithms(text, non_existing_pattern)
    
    # Візуалізація результатів
    visualize_comparison(times_existing, times_non_existing)
    
    # Зберігаємо висновки в форматі Markdown
    fastest_algorithm = min(times_existing, key=lambda x: times_existing[x]['time'])
    slowest_algorithm = max(times_existing, key=lambda x: times_existing[x]['time'])
    fastest_time = times_existing[fastest_algorithm]['time']
    slowest_time = times_existing[slowest_algorithm]['time']
    
    percent_difference = ((slowest_time - fastest_time) / fastest_time) * 100 if fastest_time > 0 else 0
    save_results_to_markdown(fastest_algorithm, slowest_algorithm, fastest_time, slowest_time, percent_difference, times_existing, times_non_existing)
