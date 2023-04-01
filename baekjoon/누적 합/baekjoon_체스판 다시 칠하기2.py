
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

A = [[0]*(M+1)]
#누적합의누적합, (N+1)*(M+1)개, 1열 & 1행의 숫자는 다 0
for i in range(1,N+1):
    s = input().rstrip()
    temp = [0] # 한 행의 누적합
    for j in range(M):
        if i%2 == 0:
            if (j%2 == 0 and s[j] == "B") or (j%2==1 and s[j] == "W"):
                temp.append(temp[j]+1)
            else:
                temp.append(temp[j])
        else:
            if (j%2 == 0 and s[j] == "B") or (j%2==1 and s[j] == "W"):
                temp.append(temp[j])
            else:
                temp.append(temp[j]+1)
            
    A.append([])
    for k in range(M+1):
        A[i].append(A[i-1][k]+temp[k])

mini = K**2
for i in range(1,N-K+2):
    for j in range(1,M-K+2):
        ans = A[K+i-1][K+j-1] - A[K+i-1][j-1] - A[i-1][K+j-1] + A[i-1][j-1]
        mini = min(mini, ans, K**2-ans)
print(mini)

## pypy로는 통과
# 누적합의 누적합인데도 시간초과... 결론 내는 과정이 (N-K)*(M-K)라 그런듯


'''import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())'''