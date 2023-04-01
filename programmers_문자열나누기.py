from multiprocessing.connection import answer_challenge
from re import X


S = input()

def solution(s):
    answer = 0
    i = 0
    while i < len(s):
        x = s[i]
        same = 1
        diff = 0
        if i == len(s)-1:
            answer += 1
            break
        else: i += 1
        
        while True:
            if i == len(s)-1:
                break
            if s[i] == x:
                same += 1
            else:
                diff += 1
            i += 1
            if same == diff:
                break
        answer += 1
        
    return answer


print(solution(S))

## 처음부터 다시

s = input()

def solution(s):
    
    i = 0
    answer = 0
    while i < len(s):
        x = s[i]
        same = 1
        diff = 0
        if i == len(s):
            answer += 1
            break
        else:
            while same != diff:
                i += 1
                if i >= len(s)-1:
                    break
                if s[i] == x:
                    same += 1
                else:
                    diff += 1
            answer += 1
            i += 1
    
    return answer
    
print(solution(s))

## 문자열 FOR문 이용

s = input()

def solution(s):
    answer = 0
    same = 0
    diff = 0
    for i in s:
        if same == diff:
            answer += 1
            x = i
        if i == x:
            same += 1
        else:
            diff += 1
    return answer

print(solution(s))