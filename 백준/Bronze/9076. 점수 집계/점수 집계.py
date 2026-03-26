n=int(input())
for i in range(n):
    A=list(map(int,input().split()))
    A.sort()
    if A[3]-A[1]>=4:
        print("KIN")
        continue
    print(A[1]+A[2]+A[3])