# import random, time
# from SearchAlgorithms import linear_search, binary_search
# from SortingAlgorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort_wrapper


# #testing search algorithms and sorting algorithms
# a = list(range(1, 1001))
# result, comparisons = linear_search(a, 1000)
# result2, comparisons2 = binary_search(a, 1000)
# print(f"Linear\nIndex: {result}\nComparisons: {comparisons}\n")
# print(f"Binary\nIndex: {result2}\nComparisons: {comparisons2}\n")


# #creating a list of numbers to sort
# b = list(range(1, 1001))
# random.shuffle(b)

# c = b.copy()
# d = b.copy()
# e = b.copy()
# f = b.copy()

# comparisons, swaps = bubble_sort(b)
# print(f"Bubble\nComparisons: {comparisons}\nSwaps: {swaps}\n")
    
# comparisons, swaps = selection_sort(c)
# print(f"Selection\nComparisons: {comparisons}\nSwaps: {swaps}\n")


# comparisons, shifts = insertion_sort(d)
# print(f"Insertion\nComparisons: {comparisons}\nShifts: {shifts}\n")

# sorted_values, comparisons = merge_sort(e)
# print(f"Merge\nComparisons: {comparisons}\n")

# comparisons, swaps = quick_sort_wrapper(f)
# print(f"Quick\nComparisons: {comparisons}\nSwaps: {swaps}\n")
