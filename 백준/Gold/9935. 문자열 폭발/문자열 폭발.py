import sys

target = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
bomb_len = len(bomb)
last_char = bomb[-1] 

for char in target:
    stack.append(char)
    
    if char == last_char and len(stack) >= bomb_len:
        if "".join(stack[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                stack.pop()

result = "".join(stack)
if result:
    print(result)
else:
    print("FRULA")