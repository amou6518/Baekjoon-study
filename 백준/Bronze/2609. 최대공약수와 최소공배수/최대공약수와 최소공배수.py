import sys

a, b = map(int, sys.stdin.readline().split())

def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def get_lcm(x, y, gcd):
    return (x * y) // gcd

gcd_val = get_gcd(a, b)
lcm_val = get_lcm(a, b, gcd_val)

print(gcd_val)
print(lcm_val)