import sys

n = int(sys.stdin.readline())

for _ in range(n):
    data = sys.stdin.readline().split()
    number = int(data[0])
    str = data[1]      

    p = ""
    
    for char in str:
        p += char *  number 
        
    print(p)