import sys
from collections import Counter

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    if not (1 <= n <= 500000) or n % 2 == 0:
        pass

    numbers = []
    for i in range(1, n + 1):
        num = int(input_data[i])
        if -4000 <= num <= 4000:
            numbers.append(num)

    if not numbers:
        return

    avg = sum(numbers) / n
    print(int(round(avg)))
    
    numbers.sort()
    print(numbers[n // 2])

    mode_dict = Counter(numbers)
    modes = mode_dict.most_common() 
    
    max_freq = modes[0][1]
    
    candidates = [val for val, freq in modes if freq == max_freq]
    candidates.sort()
    
    if len(candidates) > 1:
        print(candidates[1])
    else:
        print(candidates[0])

    print(numbers[-1] - numbers[0])

if __name__ == "__main__":
    solve()