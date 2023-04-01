A = []
L_m = 0
for _ in range(5):
    temp = input()
    L_m = max(L_m, len(temp))
    A.append(list(temp)) #list화 하면 자동으로 한글자씩이 list의 원소로 반환됨

ans = ""
for i in range(L_m):
    for j in range(5):
        if i <= len(A[j])-1: 
            ans += A[j][i]
print(ans)