import sys
input = sys.stdin.readline
N = int(input())
Plist = list(map(int,input().split()))
Plist.sort()
#누적합
Alist = [Plist[0]]
Ans = Plist[0]
for i in range(1,N):
    B = Plist[i]+Alist[-1]
    Alist.append(B)
    Ans += B
print(Ans)