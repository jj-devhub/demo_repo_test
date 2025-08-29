def sum_negative(lst):
    return sum(x for x in lst if x < 0)  # Bug fixed: sum only negative numbers

print(sum_negative([-1, 2, -3, 4, -5]))
