import sys
N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)] #겨울에 추가되는 양분
Mlist = [list(map(int,input().split())) for _ in range(M)] #[x,y,z] M개
# Global 변수 없이 풀어보자! for 프로그래머스

# 초기값 setting
Ngraph = [[5]*N for _ in range(N)] # 초기 양분
treestate = [[[] for _ in range(N)] for _ in range(N)] # 각 칸의 나무 상태
for m in Mlist:
    treestate[m[0]-1][m[1]-1].append(m[2])
    treestate[m[0]-1][m[1]-1] = sorted(treestate[m[0]-1][m[1]-1], reverse = True)
    #나이 많은 순서대로 정렬 -> 어린 순서대로 pop 가능

def spring(Ngraph,treestate,N): # 양분 먹기
    for x in range(N):
        for y in range(N):
            temp1 = [] # 성장한 나무의 나이
            temp2 = [] # 즉사한 나무의 나이
            while treestate[x][y]:
                a = treestate[x][y].pop()
                if Ngraph[x][y] >= a: # 성장 가능
                    Ngraph[x][y] -= a
                    temp1.append(a+1)
                else: # 성장 불가 -> 즉사
                    temp2.append(a)
            treestate[x][y] = [temp1[::-1],temp2] # temp1은 역순으로 저장!
                        
def summer(Ngraph,treestate,N): # 죽은 나무를 양분으로 
    for x in range(N):
        for y in range(N):
            while treestate[x][y][1]:
                a = treestate[x][y][1].pop()
                Ngraph[x][y] += a//2
            treestate[x][y] = treestate[x][y][0]
                
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
def fall(Ngraph,treestate,N,dx,dy): # 번식
    for x in range(N):
        for y in range(N):
            count = 0 #해당칸의 번식가능 나무 수
            for t in treestate[x][y]:
                if t % 5 == 0: # 번식 가능
                    count += 1
            if count > 0: #번식가능한 나무가 있다면
                for k in range(8):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0<=xx<N and 0<=yy<N:
                        for _ in range(count): #count 수 만큼
                            treestate[xx][yy].append(1) # 1인 나무 생성
    
def winter(Ngraph,N,A): # 양분추가
    for x in range(N):
        for y in range(N):
            Ngraph[x][y] += A[x][y]

for x in range(N):
    print(treestate[x])
print()
# K년 보내기
for _ in range(K):
    spring(Ngraph,treestate,N)
    summer(Ngraph,treestate,N)
    fall(Ngraph,treestate,N,dx,dy)
    winter(Ngraph,N,A)
    
    for x in range(N):
        print(Ngraph[x])
    print()
    
    for x in range(N):
        print(treestate[x])
    print()
    print()
# 나무 수 세기
M = 0
for x in range(N):
    for y in range(N):
        M += len(treestate[x][y])
print(M)