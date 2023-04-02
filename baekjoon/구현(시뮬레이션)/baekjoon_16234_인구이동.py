import sys
input = sys.stdin.readline
N,L,R = map(int,input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

def BFS(A):
    global N,L,R
    
group = [[0]*N for i in range(N)] #연합 소속이면 자연수, 아니면 0(변동없음)

