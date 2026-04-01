import sys
from collections import Counter

def solve():
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
        return

    words = [sys.stdin.readline().strip() for _ in range(n)]
    target_word = words[0]
    target_counter = Counter(target_word)
    
    similar_count = 0

    for i in range(1, n):
        compare_word = words[i]
        
        if abs(len(target_word) - len(compare_word)) > 1:
            continue
            
        compare_counter = Counter(compare_word)

        minus_cnt = 0 
        plus_cnt = 0  

        for char in set(target_word + compare_word):
            diff = target_counter[char] - compare_counter[char]
            if diff > 0:
                minus_cnt += diff
            elif diff < 0:
                plus_cnt -= diff

        if minus_cnt <= 1 and plus_cnt <= 1:
            similar_count += 1

    print(similar_count)

if __name__ == "__main__":
    solve()