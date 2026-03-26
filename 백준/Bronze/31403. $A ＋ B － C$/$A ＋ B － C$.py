import sys

a_str = sys.stdin.readline().rstrip()
b_str = sys.stdin.readline().rstrip()
c_str = sys.stdin.readline().rstrip()

a_num = int(a_str)
b_num = int(b_str)
c_num = int(c_str)
print(a_num + b_num - c_num)

ab_combined = a_str + b_str
print(int(ab_combined) - c_num)