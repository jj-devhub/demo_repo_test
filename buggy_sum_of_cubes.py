def sum_of_cubes(lst):
    return sum(x*x*x for x in lst)  # Bug fixed: sum cubes

print(sum_of_cubes([1, 2, 3]))
