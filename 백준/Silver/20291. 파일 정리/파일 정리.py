import sys
n = int(sys.stdin.readline())
extensions = {}

for i in range(n):
    file =  sys.stdin.readline().rstrip().split('.')
    ext = file[1] 

    if ext in extensions:
        extensions[ext] += 1
    else:
        extensions[ext] = 1

result = sorted(extensions.items(), key=lambda x: x[0])

for name, count in result:
    print(name, count)