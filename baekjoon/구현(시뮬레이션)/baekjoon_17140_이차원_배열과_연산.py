import sys
r,c,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(3)]

numrow = 3 # 행
numcol = 3 # 열 Max값

#R연산
def calR(A):
    global numrow, numcol
    numcol = 0
    for i in range(numrow):
        count = {i:0 for i in range(1,101)}
        for j in range(len(A[i])):
            if A[i][j]!=0:
                count[A[i][j]]+=1
        B = list(sorted(count.items(), key = lambda x:(x[1],x[0])))
        temp = []
        for k in range(100):
            if B[k][1] != 0:
                temp.append(B[k][0])
                temp.append(B[k][1])
        numcol = max(numcol, min(100,len(temp)))
        A[i] = temp[0:100] #100개까지만 넣기
#C연산
def calC(A):
    global numrow, numcol
    numrow2 = 0
    C = []
    for j in range(numcol):
        temp = []
        for i in range(numrow):
            if len(A[i]) >= j+1:
                temp.append(A[i][j])
        
        count = {i:0 for i in range(1,101)}
        for i in range(len(temp)):
            if temp[i] != 0:
                count[temp[i]]+=1
        B = list(sorted(count.items(), key = lambda x:(x[1],x[0])))
        temp2 = []
        for k in range(100):
            if B[k][1] != 0:
                temp2.append(B[k][0])
                temp2.append(B[k][1])
        numrow2 = max(numrow2, min(100,len(temp2)))
        C.append(temp2[0:100])
    # 행 수 update
    numrow = numrow2
    # A update
    A = []
    for i in range(numrow):
        temp = []
        for j in range(numcol):
            try: temp.append(C[j][i])
            except: temp.append(0)
        A.append(temp)
    return A

for time in range(101):
    #A[r][c] 체크
    if numrow >= r:
        if len(A[r-1]) >= c:
            if A[r-1][c-1] == k:
                print(time)
                exit(0)
    #연산시작
    if numrow >= numcol:
        calR(A)
    else:
        A = calC(A)


# 실패시
print(-1)