import sys
input = sys.stdin.readline
S = input().rstrip()
q = int(input())
adict = dict()

for _ in range(q):
    a,l,r = map(str,input().split())
    l = int(l)
    r = int(r)
    if a in adict.keys():
        #이미 있다면, 만들어놓은 누적합 사용
        if l == 0:
            print(adict[a][r])
        else:
            print(adict[a][r]-adict[a][l-1])
    else:
        #없다면, 새로운 누적합 생성 @ key값 = a
        adict[a] = [int(S[0]==a)]
            #1번 문자가 a이면 1, 아니면 0 저장
        for i in range(1,len(S)):
            adict[a].append( adict[a][i-1]+ int(S[i]==a) )
        adict[a].append(adict[a][-1])
            #r의 입력범위에 맞춰, 하나 더 추가
        #문제도 풀자
        if l == 0:
            print(adict[a][r])
        else:
            print(adict[a][r]-adict[a][l-1])

