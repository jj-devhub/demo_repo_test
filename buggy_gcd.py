def gcd(a, b):
    while b:
        a, b = b, a % b  # Bug fixed: use modulo, not addition
    return a

print(gcd(48, 18))
