

# Bubble sort implementation with comparison and swap counts
def bubble_sort(a):
    comparisons = 0
    swaps = 0
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for j in range(n - 1 - p):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

# Selection sort implementation with comparison and swap counts
def selection_sort(a):
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1
    return comparisons, swaps

# Insertion sort implementation with comparison and swap counts
def insertion_sort(a):
    comparisons = 0
    shifts = 0
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            comparisons += 1
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return comparisons, shifts

# Merge sort implementation with comparison count

def merge_sort(values):
    if len(values) <= 1:
        return values, 0
    mid = len(values) // 2
    left, lc = merge_sort(values[:mid])
    right, rc = merge_sort(values[mid:])
    merged = []
    i = j = 0
    comparisons = lc + rc
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comparisons

# Quick sort implementation with comparison and swap counts
def quick_sort_wrapper(values):
    global quick_comparisons, quick_swaps
    quick_comparisons = 0
    quick_swaps = 0
    quick_sort(values, 0, len(values) - 1)
    return quick_comparisons, quick_swaps

quick_comparisons = 0
quick_swaps = 0
def partition(values, low, high):
    global quick_comparisons, quick_swaps
    pivot = values[high]
    i = low - 1
    for j in range(low, high):
        quick_comparisons += 1
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
            quick_swaps += 1
    values[i + 1], values[high] = values[high], values[i + 1]
    quick_swaps += 1
    return i + 1
def quick_sort(values, low, high):
    global quick_comparisons, quick_swaps
    if low < high:
        p = partition(values, low, high)
        quick_sort(values, low, p - 1)
        quick_sort(values, p + 1, high)
    return quick_comparisons, quick_swaps