T = int(input())
arr = [[0 for _ in range(14)] for _ in range(14)]
for i in range(14):
    arr[0][i] = i+1
for j in range(1,14):
    for i in range(14):
        arr[j][i] = sum(arr[j-1][0:i+1])
for _ in range(T):
    k = int(input())
    n = int(input())
    print(arr[k-1][n-1])