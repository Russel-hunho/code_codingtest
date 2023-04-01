A,B = map(int,input().split())
ans = []
i = 1001
while i > 0:
    ans.append(str(A//B))
    A = (A%B)*10
    i -= 1
print( "".join([ ans[0], "."] + ans[1:-1]) )