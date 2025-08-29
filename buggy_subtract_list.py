def subtract_list(lst):
    if not lst:
        return 0
    result = lst[0]
    for num in lst[1:]:
        result -= num  # Bug fixed: subtract from first element
    return result

print(subtract_list([10, 2, 3]))
