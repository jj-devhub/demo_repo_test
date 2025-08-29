def average_of_squares(lst):
    return sum(x*x for x in lst) / len(lst)  # Bug fixed: average of squares

print(average_of_squares([2, 4, 6]))
