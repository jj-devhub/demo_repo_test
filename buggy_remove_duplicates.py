def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result  # Bug fixed: preserves order

print(remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5]))
