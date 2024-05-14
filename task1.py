import random
import timeit

#Merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


#Insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Генеруємо тестові дані
data = random.sample(range(1, 10000), 1000)

# Вимірюємо час для сортування злиттям
merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)

# Вимірюємо час для сортування вставками
insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)

# Вимірюємо час для вбудованого алгоритму Timsort
timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

# Виводимо результати
print(f"Час сортування злиттям: {merge_sort_time}")
print(f"Час сортування вставками: {insertion_sort_time}")
print(f"Час виконання Timsort (вбудований в Python): {timsort_time}")