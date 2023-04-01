import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

class queue():
    def __init__(self):
        self.queue = deque()
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
        return None
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    
    def push(self,n):
        self.queue.append(n)
        return None
    def pop(self):
        if self.isEmpty():
            print(-1)
        else:
            a = self.queue.popleft()
            print(a)
        return None
    def size(self):
        print(len(self.queue))
        return None
    def empty(self):
        if self.isEmpty():
            print(1)
        else:
            print(0)
        return None
    def front(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.queue[0])
        return None
    def back(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.queue[-1])
        return None
    
que = queue()
for _ in range(N):
    S = input().rstrip()
    que.do(S)