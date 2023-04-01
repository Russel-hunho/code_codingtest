N,M = map(int,input().split())
ans = [i+1 for i in range(N)]
for _ in range(M):
    i,j,k = map(int,input().split())
    temp = []
    for a in range(j-i+1):
        temp.append(ans[(i-1)+a])
        if k+a <= j:    # a = j-k까지, 총j-k+1번 (j부터 k까지)            
            ans[(i-1)+a] = ans[(k-1)+a]
        else:
            ans[(i-1)+a] = temp[a-(j-k+1)]
for b in ans:
    print(b, end=" ")