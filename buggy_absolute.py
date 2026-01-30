def absolute(x):
    if x < 0:
        return -x  # Bug fixed: now returns -x for negative
    return x

print(absolute(-5))
