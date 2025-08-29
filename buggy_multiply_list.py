def multiply_list(lst):
    result = 0  # Bug: should start with 1
    for num in lst:
        result += num  # Bug: should multiply, not add
    return result

print(multiply_list([2, 3, 4]))
