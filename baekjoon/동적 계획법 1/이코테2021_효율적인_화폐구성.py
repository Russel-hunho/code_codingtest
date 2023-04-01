##https://www.youtube.com/watch?v=5Lu34WIx2Us&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 43:29

'''일반 풀이 -> 특수성에 대해 잘못고려해서 틀림.
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Nlist = []
for _ in range(N):
    Nlist.append(int(input()))
Nlist.sort(reverse = True)

state = 1
i = 0
count = 0
while True:
    if M < Nlist[-1]:
        if M == 0:
            state = 0
            break
        else:
            state = -1
            break
    if M%Nlist[i] == 0:
        count += M//Nlist[i]
        M %= Nlist[i]
    i += 1
if state == 0:
    print(count)
else:
    print(-1)
'''

#DP 풀이
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Nlist = []
for _ in range(N):
    Nlist.append(int(input()))
Nlist.sort()

DP = [0]*(M+1)

def money(M):
    for j in range(1,Nlist[0]): #min값보다 작으면
        DP[j] = -1
    for j in range(Nlist[0],M+1): #M까지
        for k in Nlist:
            for a in range(k,M+1,k):
                if DP[j-a] != -1:
                    if DP[j] == 0:
                        DP[j] = DP[j-a]+a//k
                    else:
                        DP[j] = min( DP[j], DP[j-a]+a//k )
    return DP[M]
    
print(money(M))
