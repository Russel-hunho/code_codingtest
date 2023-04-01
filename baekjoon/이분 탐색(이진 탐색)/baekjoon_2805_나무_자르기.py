import sys
input = sys.stdin.readline
N,M = map(int,input().split())
Nlist = list(map(int,input().split()))
start = 1
end = max(Nlist)
while True:
    if start > end:
        break
    mid = (start+end)//2
    count = 0
    for i in Nlist:
        if i > mid:
            count += i - mid
    if count >= M:
        H = mid
        start = mid + 1
    else:
        end = mid - 1
print(H)