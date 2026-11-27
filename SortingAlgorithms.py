

import time
from Comparison import print_table, preview
from Validation import verify_sort


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
        # Count every comparison, including the one that stops the shifting
        while j >= 0:
            comparisons += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return comparisons, shifts

# Merge sort implementation with comparison and move counts
# (moves = elements written into the merged list, since merge sort doesn't swap)
def merge_sort(values):
    if len(values) <= 1:
        return values, 0, 0
    mid = len(values) // 2
    left, lc, lm = merge_sort(values[:mid])
    right, rc, rm = merge_sort(values[mid:])
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
    return merged, comparisons, lm + rm + len(merged)

# Quick sort implementation with comparison, swap and partition counts
def quick_sort_wrapper(values):
    stats = {"comparisons": 0, "swaps": 0, "partitions": 0}
    quick_sort(values, 0, len(values) - 1, stats)
    return stats["comparisons"], stats["swaps"], stats["partitions"]


def swap(values, i, j, stats):
    # Only count real swaps, not an element swapped with itself
    if i != j:
        values[i], values[j] = values[j], values[i]
        stats["swaps"] += 1


def median_of_three(values, low, high, stats):
    # Move the median of the first, middle and last elements to values[high]
    # so sorted and reverse-sorted input don't give the worst-case pivot
    mid = (low + high) // 2
    stats["comparisons"] += 1
    if values[mid] < values[low]:
        swap(values, low, mid, stats)
    stats["comparisons"] += 1
    if values[high] < values[low]:
        swap(values, low, high, stats)
    stats["comparisons"] += 1
    if values[mid] < values[high]:
        swap(values, mid, high, stats)


def partition(values, low, high, stats):
    stats["partitions"] += 1
    if high - low >= 2:
        median_of_three(values, low, high, stats)
    pivot = values[high]
    i = low - 1
    for j in range(low, high):
        stats["comparisons"] += 1
        if values[j] <= pivot:
            i += 1
            swap(values, i, j, stats)
    swap(values, i + 1, high, stats)
    return i + 1


def quick_sort(values, low, high, stats):
    # Recurse into the smaller side and loop on the larger one,
    # so the recursion depth stays O(log n) even in the worst case
    while low < high:
        p = partition(values, low, high, stats)
        if p - low < high - p:
            quick_sort(values, low, p - 1, stats)
            low = p + 1
        else:
            quick_sort(values, p + 1, high, stats)
            high = p - 1

def test_sorting_algorithms(data):
    print("\nTesting Sorting Algorithms -- Bubble, Selection, Insertion, Merge and Quick Sort")
    print(f"Original data: {preview(data)}")

    # Each algorithm gets its own copy so they all start with the same data
    a = data.copy()
    start_time = time.perf_counter()
    comparisons, swaps = bubble_sort(a)
    end_time = time.perf_counter()
    rows = [["Bubble Sort", comparisons, swaps, "-", f"{end_time - start_time:.6f}", "Yes" if verify_sort(data, a) else "NO"]]

    a = data.copy()
    start_time = time.perf_counter()
    comparisons, swaps = selection_sort(a)
    end_time = time.perf_counter()
    rows.append(["Selection Sort", comparisons, swaps, "-", f"{end_time - start_time:.6f}", "Yes" if verify_sort(data, a) else "NO"])

    a = data.copy()
    start_time = time.perf_counter()
    comparisons, shifts = insertion_sort(a)
    end_time = time.perf_counter()
    rows.append(["Insertion Sort", comparisons, shifts, "-", f"{end_time - start_time:.6f}", "Yes" if verify_sort(data, a) else "NO"])

    a = data.copy()
    start_time = time.perf_counter()
    sorted_values, comparisons, moves = merge_sort(a)
    end_time = time.perf_counter()
    rows.append(["Merge Sort", comparisons, moves, "-", f"{end_time - start_time:.6f}", "Yes" if verify_sort(data, sorted_values) else "NO"])

    a = data.copy()
    start_time = time.perf_counter()
    comparisons, swaps, partitions = quick_sort_wrapper(a)
    end_time = time.perf_counter()
    rows.append(["Quick Sort", comparisons, swaps, partitions, f"{end_time - start_time:.6f}", "Yes" if verify_sort(data, a) else "NO"])

    print()
    print_table(["Algorithm", "Comparisons", "Swaps/Shifts/Moves", "Partitions", "Time (s)", "Correct"], rows)

    print(f"\nSorted result: {preview(sorted_values)}")
