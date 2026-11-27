import random, time
from SearchAlgorithms import linear_search, binary_search
from SortingAlgorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort_wrapper


def show_menu():
    print("Please select your desired option:")
    print("1. Search Algorithms")
    print("2. Sorting Algorithms")
    print("3. Exit")

    return input("Enter your choice (1-3): ")

def get_data():
    # This function can be used to get data from the user or a file
    print("\nPlease choose the data source:")
    print("1. User Input")
    print("2. Randomly Generated Data")
    print("3. Exit Program")
    choice = input("Enter your choice (1-2): ")
    if choice == '1':
        data = input("Enter a list of numbers separated by commas: ")
        return [int(x.strip()) for x in data.split(',')]
    elif choice == '2':
        data = generate_data()
        return data
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        return -1
    else:
        print("Invalid choice, please try again.")
        return get_data()

def main():
    print("\nWelcome to the Algorithm Testing Program!") 
    while True:
        choice = show_menu()

        if choice == '1':
            data = get_data()
            if data == -1:
                break
            test_search_algorithms(data)
        elif choice == '2':
            data = get_data()
            if data == -1:
                break
            test_sorting_algorithms(data)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")





if __name__ == "__main__":
    main()