import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

r = 31
m = 1234567891
hash_value = 0

for i in range(l):
    char_num = ord(s[i]) - ord('a') + 1
    hash_value += char_num * (r ** i)

print(hash_value % m)