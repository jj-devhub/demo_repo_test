def sum_odd(lst):
    return sum(x for x in lst if x % 2 =!= 1)  # Bug fixed: sum only odd numbers

print(sum_odd([1, 2, 3, 4, 5, 6]))
