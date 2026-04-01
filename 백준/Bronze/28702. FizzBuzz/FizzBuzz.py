import sys

inputs = [sys.stdin.readline().strip() for _ in range(3)]
next_number = 0

for i in range(3):
    if inputs[i].isdigit():
        next_number = int(inputs[i]) + (3 - i)
        break

if next_number % 3 == 0 and next_number % 5 == 0:
    print("FizzBuzz")
elif next_number % 3 == 0:
    print("Fizz")
elif next_number % 5 == 0:
    print("Buzz")
else:
    print(next_number)