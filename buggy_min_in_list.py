def min_in_list(lst):
    if not lst:
        return None
    min_val = lst[0]  # Bug fixed: use first element
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val

print(min_in_list([5, 2, 8]))
