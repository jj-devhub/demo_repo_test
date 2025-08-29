def find_second_largest(numbers):
    # Bug fixed: handle duplicate values by using set to get unique numbers
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None  # Not enough unique numbers
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

def find_nth_largest(numbers, n):
    # Bug fixed: handle case when n > length of unique numbers
    unique_numbers = sorted(set(numbers), reverse=True)
    if n > len(unique_numbers) or n <= 0:
        return None  # Invalid n value
    return unique_numbers[n-1]

test_list = [5, 2, 8, 8, 1, 9]
print(f"Second largest in {test_list}: {find_second_largest(test_list)}")

test_list2 = [1, 2, 3]
print(f"5th largest in {test_list2}: {find_nth_largest(test_list2, 5)}")
