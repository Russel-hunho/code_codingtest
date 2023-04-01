N = int(input())
for i in range(666,1000000*N+666):
    if "666" in str(i):
        N -= 1
    if N == 0:
        print(i)
        break