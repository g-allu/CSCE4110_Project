import math
from collections import Counter


# ---------- Input validation ----------
# Each function keeps asking until the user gives a valid answer.

def parse_number(text):
    # Return the number in text, or None if it isn't a real, finite number
    try:
        value = float(text.strip())
    except ValueError:
        return None
    if math.isnan(value) or math.isinf(value):
        return None
    return value


def get_menu_choice(prompt, options):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print(f"Invalid choice. Please enter one of: {', '.join(options)}")


def get_int(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Please enter a number between {minimum} and {maximum}.")


def get_number(prompt):
    while True:
        value = parse_number(input(prompt))
        if value is not None:
            return value
        print("Please enter a valid number.")


def get_number_list(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("The list can't be empty.")
            continue
        parts = text.split(',')
        values = [parse_number(p) for p in parts]
        bad = [p.strip() for p, v in zip(parts, values) if v is None]
        if bad:
            shown = ", ".join(f"'{b}'" for b in bad)
            print(f"Only numbers are allowed. Invalid entries: {shown}")
            continue
        return values


def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please enter y or n.")


# ---------- Output validation ----------

def is_sorted(a):
    # Check that every element is <= the one after it
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


def verify_sort(original, result):
    # The result must be in order and contain exactly the same elements
    return is_sorted(result) and Counter(original) == Counter(result)


def verify_search(data, target, index):
    # Use Python's "in" operator as the reference answer
    if target in data:
        return 0 <= index < len(data) and data[index] == target
    return index == -1
