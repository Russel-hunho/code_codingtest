from dataclasses import asdict


X = 100
Y = 2030450

def solution(X, Y):
    answer = ''
    xlist = list(str(X))
    ylist = list(str(Y))
    collect = []
    while True:
        if len(xlist) == 0:
            break
        elif xlist[0] in ylist:
            collect.append(xlist[0])
            ylist.remove(xlist[0])
            xlist.pop(0)
        else:
            xlist.pop(0)
    
    if len(collect) == 0:
        return "-1"
    
    collect.sort()
    collect.reverse()
    answer = ''.join(collect) 
    answer = str(int(answer)) #00 같은 case 제거
    
    return answer

print(solution(X,Y))

##시간초과뜸..

X = 100
Y = 2030450

from collections import Counter as ct

def solution(X, Y):
    answer = ''
    xlist = list(str(X))
    ylist = list(str(Y))
    collect = dict()
    xdict = dict(ct(xlist))
    ydict = dict(ct(ylist))
    for i in list(xdict.keys()):
        if i in list(ydict.keys()):
            collect[i] = min( xdict[i], ydict[i] )
    
    if len(collect) == 0:
        return "-1"
    
    tot = []
    for j in collect.keys():
        for _ in range(collect[j]):
            tot.append(j)
    
    tot.sort()
    tot.reverse()
    answer = ''.join(tot)
    answer = str(int(answer))
    
    return answer

print(solution(X,Y))


### 더 줄여보기... 
X = "100"
Y = "2030450"

def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        xcount = X.count(str(i))
        ycount = Y.count(str(i))
        i_count = min (xcount,ycount)
        if i_count > 0:
            answer = ''.join([answer,str(i)*i_count])

    if answer == "":
        return "-1"
    elif int(answer) == 0:
        return "0"
    else:
        return answer

print(solution(X,Y))

#마지막으로 더 줄이기: 000을 0으로 반환할 때, int 반환 시간이 꽤 걸림..
X = "100"
Y = "2030450"

def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        xcount = X.count(str(i))
        ycount = Y.count(str(i))
        i_count = min (xcount,ycount)
        if i_count > 0:
            answer = ''.join([answer,str(i)*i_count])

    if answer == "":
        return "-1"
    elif answer[0] == 0:
        return "0"
    else:
        return answer

print(solution(X,Y))