import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(1000000)
    #재귀의 반복 횟수의 최댓값 = 기본 1000, 현 문제에선 1000000까지 늘려줘야함!

class AC():
    def __init__(self):
        self.AC = 1 # state로 활용
            #self.AC == 1: 정순(left) / 0: 역순(right) / -1: 에러
        return None
        
    def do(self, xqueue, pqueue):
        if len(pqueue) == 0:
            return 0
        elif len(xqueue) == 0 and pqueue[0] == "D":
            self.AC = -1
            return 0 # error 출력 예정
        else:
            doit = pqueue.popleft()
            if doit == "D":
                if self.AC == 1:
                    xqueue.popleft()
                else: #역순
                    xqueue.pop()
            elif doit == "R":
                self.AC = 1-self.AC #1이면 0으로, 0이면 1로
        return self.do(xqueue,pqueue)
    
    def state(self):
        return self.AC

T = int(input())
for _ in range(T):
    pqueue = deque(list(input().rstrip()))
    n = int(input())
    xlist = input().rstrip().lstrip("[").rstrip("]")
    if len(xlist) == 0:
        xqueue = deque()
    elif len(xlist) == 1:
        xqueue = deque([int(xlist)])
    else:
        xqueue = deque(map(int,xlist.split(",")))
    
    A = AC()
    A.do(xqueue,pqueue)
    state = A.state()
    
    if state == -1:
        print("error",end = "")
    elif len(xqueue) == 0:
        print("[]",end = "")
    elif len(xqueue) == 1:
        print("[{}]".format(xqueue[0]),end = "")
    else:
        print("[",end = "")
        if state == 0: # 역순
            xqueue.reverse()
        for i in list(xqueue)[0:-1]:
            print(i,end=",")
        print(xqueue[-1],end="]")
    print()