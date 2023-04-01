## 개인정보 수집 유효기간
Today = input()
Terms = list(map(str,input().split())
Privacies = list(input())

def solution(today, terms, privacies):
    year, month, date = map(int, today.split(".")) # 오늘날짜
    typ = []
    due = []
    for j in range(len(terms)):
        A,B = map(str, terms[j].split())
        typ.append(A)
        due.append(int(B))
    answer = []
    for i in range(len(privacies)):
        pri_year, pri_month, pri_date = map(int, privacies[i][0:10].split("."))
        pri_typ = privacies[i][11]
        pri_due = due[typ.index(pri_typ)]
        
        priday = (year - pri_year)*12*30 + (month-pri_month-pri_due)*30 + (date - pri_date)
        if priday >= 0:
            answer.append(i+1)
    return answer

print(solution(Today,Terms,Privacies))
# 좀 더 짧게




## 크기가 작은 부분문자열

T = input()
P = input()

def solution(t,p):
    answer = 0
    for j in range( len(t)-len(p)+1 ):
        num = 0
        for k in range(len(p)):
            num += 10**(len(p)-k-1) * int(t[j+k])
        if num <= int(p):
            answer += 1
    return answer

print(solution(T,P))


## 가장 가까운 같은 글자
X = input()

def solution(s):
    answer = [-1]
    for i in range(1,len(s)):
        for j in range(i-1,-1,-1):
            if s[j] == s[i]:
                answer.append( i-j )
                break
            elif j == 0:
                answer.append( -1 )
    return answer

print(solution(X))
# 시간 줄이기
X = input()

def solution(s):
    answer = []
    
    
    re

print(solution(X))