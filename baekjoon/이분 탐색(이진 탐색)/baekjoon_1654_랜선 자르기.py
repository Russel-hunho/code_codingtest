import sys
input = sys.stdin.readline
K,N = map(int,input().split())
Klist = []
for _ in range(K):
    Klist.append(int(input()))

end = max(Klist)
start = max(1,min(Klist)//(N//K+1))

while True:
    if start > end:
        break
    mid = (start+end)//2
    count = 0
    for i in Klist:
        count += i//mid
    if count >= N:
        ans = mid
        start = mid+1
    else:
        end = mid-1
print(ans)