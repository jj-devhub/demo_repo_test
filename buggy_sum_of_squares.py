def sum_of_squares(lst):
    return sum(x*x for x in lst)  # Bug fixed: sum squares

print(sum_of_squares([1, 2, 3]))
