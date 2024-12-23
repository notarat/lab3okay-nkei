import tkinter as tk
from tkinter import messagebox
import random
import time
import os

# Алгоритмы поиска

def linear_search(arr, target):
    for i in range(len(arr)):
        time.sleep(0.00001)  # Искусственная задержка
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        time.sleep(0.00001)  # Искусственная задержка
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        time.sleep(0.00001)  # Искусственная задержка
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def ternary_search(arr, l, r, x):
    while left <= right:
        time.sleep(0.00001)  # Искусственная задержка
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1
    

def fibonacci_search(arr, x):
    # Реализация поиска Фибоначчи с добавлением задержки
    return -1  # Простая заглушка, добавьте свою реализацию

def start_search():
    try:
        size = 1000000
        min_value = 0
        max_value = 10000
        target = random.randint(min_value, max_value)

        array = sorted(random.sample(range(min_value, max_value), size))

        results = []

# Генерация массива
def generate_array(size, min_value, max_value):
    try:
        array = [random.randint(min_value, max_value) for _ in range(size)]
        return array
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except Exception as e:
        print(f"Произошла другая ошибка: {e}")

# Чтение из файла
def read_array_from_file(file_path):
    if not os.path.exists(file_path):
        messagebox.showerror("Ошибка", "Файл не найден")
        return []

    with open(file_path, 'r') as file:
        return list(map(int, file.read().splitlines()))

# Запись результатов в файл
def write_results_to_file(results, file_path):
    with open(file_path, 'w') as file:
        for line in results:
            file.write(line + '\n')

# Главный интерфейс
def start_search():
    size = 1000000
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    target = random.randint(min_value, max_value + 100)  # Искать элемент, который может не существовать

    array = generate_array(size, min_value, max_value)
    array.sort()

    results = []

    # Линейный поиск
    start_time = time.perf_counter()
    index = linear_search(array, target)
    elapsed_time = time.perf_counter() - start_time
    results.append(f"Линейный поиск: {index}, время: {elapsed_time:.8f}s")

    # Бинарный поиск
    start_time = time.perf_counter()
    index = binary_search(array, target)
    elapsed_time = time.perf_counter() - start_time
    results.append(f"Бинарный поиск: {index}, время: {elapsed_time:.8f}s")

    # Тринарный поиск
    start_time = time.perf_counter()
    index = ternary_search(array, 0, len(array)-1, target)
    elapsed_time = time.perf_counter() - start_time
    results.append(f"Тринарный поиск: {index}, время: {elapsed_time:.8f}s")

    # Поиск Фибоначчи
    start_time = time.perf_counter()
    index = fibonacci_search(array, target)
    elapsed_time = time.perf_counter() - start_time
    results.append(f"Поиск Фибоначчи: {index}, время: {elapsed_time:.8f}s")

    write_results_to_file(results, "results.txt")
        messagebox.showinfo("Результаты", "\n".join(results))
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

# Основной интерфейс Tkinter
app = tk.Tk()
app.title("Алгоритмы поиска")

tk.Label(app, text="Минимальное значение:").pack()
min_entry = tk.Entry(app)
min_entry.pack()

tk.Label(app, text="Максимальное значение:").pack()
max_entry = tk.Entry(app)
max_entry.pack()

tk.Label(app, text="Искать число:").pack()
target_entry = tk.Entry(app)
target_entry.pack()
tk.Button(app, text="Начать поиск", command=start_search).pack()
app.mainloop()
