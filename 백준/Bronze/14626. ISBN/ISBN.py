import sys

isbn = sys.stdin.readline().strip()
for num in range(10):
    total = 0
    target_isbn = isbn.replace('*', str(num))

    for i in range(13):
        digit = int(target_isbn[i])
        if i % 2 == 0: 
            total += digit * 1
        else:         
            total += digit * 3

    if total % 10 == 0:
        print(num)
        break