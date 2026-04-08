import sys

n = int(sys.stdin.readline())

def is_good_sequence(seq):
    length = len(seq)
    for i in range(1, length // 2 + 1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True

def backtracking(seq):
    if len(seq) == n:
        print(seq)
        sys.exit() 

    for char in ['1', '2', '3']:
        next_seq = seq + char
        if is_good_sequence(next_seq):
            backtracking(next_seq)

backtracking("")