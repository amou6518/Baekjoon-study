import sys
n = int(sys.stdin.readline())
books = {}

for i in range(n):
    title = sys.stdin.readline().rstrip()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

result = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])