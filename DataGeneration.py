import numpy as np
from Validation import get_int, get_menu_choice

MAX_SIZE = 10000


def generate_data():
    size = get_int(f"Enter the size of the list (1-{MAX_SIZE}): ", 1, MAX_SIZE)

    print("\nPlease choose the type of data:")
    print("1. Random")
    print("2. Sorted")
    print("3. Nearly Sorted")
    print("4. Reverse Sorted")
    choice = get_menu_choice("\nEnter your choice (1-4): ", ['1', '2', '3', '4'])

    data = np.random.randint(1, size * 10 + 1, size)

    if choice == '2':
        data.sort()
    elif choice == '3':
        data.sort()
        # Swap about 5% of the elements to leave the list nearly sorted
        for _ in range(max(1, size // 20)):
            i, j = np.random.randint(0, size, 2)
            data[i], data[j] = data[j], data[i]
    elif choice == '4':
        data = np.sort(data)[::-1]

    # Convert to a regular Python list so it works with the algorithms
    return data.tolist()
