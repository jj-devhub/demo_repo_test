def max_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]  # Bug fixed: use first element
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(max_in_list([-5, -2, -1]))
 # Minimal change: added a comment
