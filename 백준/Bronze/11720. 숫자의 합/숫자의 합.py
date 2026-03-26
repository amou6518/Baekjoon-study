import sys

n= int(sys.stdin.readline())
numbers = sys.stdin.readline().rstrip()
list_numbers = list(map(int, numbers))
print(sum(list_numbers))