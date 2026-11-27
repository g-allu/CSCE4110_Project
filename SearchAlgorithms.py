

import time
from Comparison import print_table, preview
from Validation import get_number, get_yes_no, is_sorted, verify_search


# Linear Search Algorithm
def linear_search(a, target):
    comparisons = 0
    for i in range(len(a)):
        comparisons += 1
        if a[i] == target:
            return i, comparisons
    return -1, comparisons
    
# Binary Search Algorithm
def binary_search(a, target):
    left = 0
    right = len(a) - 1
    comparisons = 0
    while left <= right:
        mid = left + (right - left) // 2
        comparisons += 1
        if a[mid] == target:
            return mid, comparisons
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons   




def test_search_algorithms(data):
    print("\nTesting Search Algorithms -- Linear and Binary Search")

    # Binary search needs sorted input, so check before running it
    data_is_sorted = is_sorted(data)

    while True:
        print(f"\nData: {preview(data)}")
        if not data_is_sorted:
            print("Warning: binary search cannot run on unsorted data. Only linear search will run.")

        target = get_number("\nEnter the target number to search for: ")

        start_time = time.perf_counter()
        result, comparisons = linear_search(data, target)
        end_time = time.perf_counter()
        correct = verify_search(data, target, result)
        rows = [["Linear Search", result, comparisons, f"{end_time - start_time:.6f}",
                 "Yes" if correct else "NO"]]

        if data_is_sorted:
            start_time = time.perf_counter()
            result2, comparisons2 = binary_search(data, target)
            end_time = time.perf_counter()
            correct2 = verify_search(data, target, result2)
            rows.append(["Binary Search", result2, comparisons2, f"{end_time - start_time:.6f}",
                         "Yes" if correct2 else "NO"])

        print()
        print_table(["Algorithm", "Index", "Comparisons", "Time (s)", "Correct"], rows)
        print()

        if not get_yes_no("Do you want to search for another number? (y/n): "):
            print("Back to the menu!")
            break
