N = int(input())

def tiling(N):
    if N%2 == 1:
        return 0
    else:
        k = N//2
        D = [1,3] #N = 0,2 / k = 0,1
        for i in range(2,k+1): # 2부터 k까지
            A = D[i-1]
            for j in range(i):
                A += 2*D[j]
            D.append(A)
        return D[k]
print(tiling(N))