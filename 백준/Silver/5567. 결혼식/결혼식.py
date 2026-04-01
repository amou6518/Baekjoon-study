import sys

def solve():
    n = int(sys.stdin.readline()) 
    m = int(sys.stdin.readline())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    invite = set()

    friends = adj[1]
    for friend in friends:
        invite.add(friend) 

        for f_of_friend in adj[friend]:
            if f_of_friend != 1: 
                invite.add(f_of_friend) 

    print(len(invite))

if __name__ == "__main__":
    solve()