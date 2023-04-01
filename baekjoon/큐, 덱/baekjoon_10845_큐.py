import sys
input = sys.stdin.readline
from collections import deque

class que():
    def __init__(self):
        self.que = deque()
        return None
    
    def do(self, S):
        if "push" in S:
            n = int(S.split()[1])
            self.push(n)
        elif S == "pop":
            self.pop()
        elif S == "size":
            self.size()
        elif S == "empty":
            self.empty()
        elif S == "front":
            self.front()
        elif S == "back":
            self.back()
        return 0
            
    def isEmpty(self):
        if len(self.que) == 0:
            return 1
        else:
            return 0
    
    def push(self,n):
        self.que.append(n)
        return 0
    def pop(self):
        if self.isEmpty():
            print(-1)
        else:
            a = self.que.popleft()
            print(a)
        return 0
    def size(self):
        print(len(self.que))
        return 0
    def empty(self):
        if self.isEmpty():
            print(1)
        else:
            print(0)
        return 0
    def front(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.que[0])
        return 0
    def back(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.que[-1])
        return 0

N = int(input())
q = que()
for _ in range(N):
    S = input().rstrip()
    q.do(S)