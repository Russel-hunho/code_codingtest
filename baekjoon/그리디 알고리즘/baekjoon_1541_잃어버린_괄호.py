import sys
Slist = list(map(str,sys.stdin.readline().split("-")))
ans = 0
for i in range(len(Slist)):
    s = Slist[i]
    if "+" in s:
        s_numlist = list(map(int,s.split("+")))
        K = sum(s_numlist)
    else:
        K = int(s)
    if i == 0:
        ans += K
    else:
        ans -= K
print(ans)