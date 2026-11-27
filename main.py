from SearchAlgorithms import test_search_algorithms
from SortingAlgorithms import test_sorting_algorithms
from DataGeneration import generate_data
from Validation import get_menu_choice, get_number_list


def show_menu():
    print("\nPlease select your desired option:")
    print("1. Search Algorithms")
    print("2. Sorting Algorithms")
    print("3. Exit")

    return get_menu_choice("\nEnter your choice (1-3): ", ['1', '2', '3'])


def get_data():
    # Returns the data to use, or None if the user wants to go back
    print("\nPlease choose the data source:")
    print("1. User Input")
    print("2. Randomly Generated Data")
    print("3. Back to Main Menu")
    choice = get_menu_choice("\nEnter your choice (1-3): ", ['1', '2', '3'])

    if choice == '1':
        return get_number_list("Enter a list of numbers separated by commas: ")
    if choice == '2':
        return generate_data()
    return None


def main():
    print("\nWelcome to the Algorithm Testing Program!")
    while True:
        choice = show_menu()

        if choice == '3':
            print("Exiting the program. Goodbye!")
            break

        data = get_data()
        if data is None:
            continue

        if choice == '1':
            test_search_algorithms(data)
        else:
            test_sorting_algorithms(data)


if __name__ == "__main__":
    main()
