import sys

n = int(sys.stdin.readline())
word_set = set()
for _ in range(n):
    word_set.add(sys.stdin.readline().strip())

word_list = list(word_set)
word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)