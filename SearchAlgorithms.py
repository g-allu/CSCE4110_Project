

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


