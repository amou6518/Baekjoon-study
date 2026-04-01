import sys

def get_sum(serial):
    total = 0
    for char in serial:
        if char.isdigit(): 
            total += int(char)
    return total

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)

    serials = []
    for _ in range(n):
        serials.append(sys.stdin.readline().strip())
    serials.sort(key=lambda x: (len(x), get_sum(x), x))
    for s in serials:
        print(s)

if __name__ == "__main__":
    solve()