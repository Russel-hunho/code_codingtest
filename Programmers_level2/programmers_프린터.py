'''
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다
    중요도가 높은 문서가 한 개라도 존재하면
    J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
인쇄 작업의 중요도는 1~9로 표현하며
숫자가 클수록 중요하다는 뜻입니다.
'''

priorities = [2, 1, 3, 2]
location = 2

priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    answer = 1
    while True:
        m = max(priorities)
        i = priorities.index(m)
        if i == location:
            return answer
        if i == 0:
            location -= 1
            priorities.pop(0)
        else:
            priorities = priorities[i+1:]+priorities[0:i]
            if i < location:
                location -= (i+1)
            else:
                location += -i+len(priorities)
        answer += 1



print(solution(priorities, location))