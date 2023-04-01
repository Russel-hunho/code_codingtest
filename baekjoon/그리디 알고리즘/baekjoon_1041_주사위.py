import sys
from itertools import combinations as cb
input = sys.stdin.readline
n = int(input())
sixlist = list(map(int,input().split()))
if n == 1:
    print(sum(sixlist)-max(sixlist))
else:
    a = min(sixlist)
    b = 100
    for i in set(cb([j for j in range(6)],2)) - set([(0,5),(1,4),(2,3)]):
        b = min( b, sixlist[i[0]] + sixlist[i[1]] )
    c = 150
    for i in [[0,1,2],[0,1,3],[0,2,4],[0,3,4],[5,1,2],[5,1,3],[5,2,4],[5,3,4]]:
        c = min( c, sixlist[i[0]] + sixlist[i[1]] + sixlist[i[2]] )
    ans = ((n-2)**2*5+(n-2)*4)*a
    ans += ((n-2)*8+4)*b
    ans += 4 * c
    print(ans)