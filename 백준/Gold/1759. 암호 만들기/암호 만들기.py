import sys

l, c = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
answer = []

def backtracking(idx, current_pw):
    if len(current_pw) == l:
        v_count = 0
        c_count = 0 
        
        for char in current_pw:
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
        
        if v_count >= 1 and c_count >= 2:
            print("".join(current_pw))
        return

    for i in range(idx, c):
        current_pw.append(chars[i])
        backtracking(i + 1, current_pw) 
        current_pw.pop() 

backtracking(0, [])