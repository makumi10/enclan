# Question 1 - remove duplicates from a list and sort it

def dedupe_and_sort(numbers):
    unique_numbers = set(numbers)   # a set can't hold duplicates
    return sorted(unique_numbers)   # then just sort it


if __name__ == "__main__":
    numbers = [12, 7, 12, 3, 5, 7, 8, 3, 9]
    result = dedupe_and_sort(numbers)
    print("Original list:", numbers)
    print("Result:", result)
