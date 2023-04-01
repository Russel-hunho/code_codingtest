n = int(input())
N = 0
for i in range(1,n-1):
    N += (n-i)*(n-i-1)//2
print(N,3)