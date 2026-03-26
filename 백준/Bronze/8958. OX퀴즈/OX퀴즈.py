import sys

n = int(sys.stdin.readline())
for _ in range(n):
    result = sys.stdin.readline().rstrip()
    total_score = 0  
    current_score = 0 

    for char in result:
        if char == 'O':
            current_score += 1   
            total_score += current_score
        else:
            current_score = 0   

    print(total_score)