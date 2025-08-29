def sum_even(lst):
    return sum(x for x in lst if x % 2 == 0)  # Bug fixed: sum only even numbers

print(sum_even([1, 2, 3, 4, 5, 6]))
