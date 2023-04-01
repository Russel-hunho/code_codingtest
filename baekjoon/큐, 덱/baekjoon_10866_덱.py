from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

class dequ():
    def __init__(self):
        self.dequ = deque()
        return None
    
    def do(self, S):
        if "push" in S:
            A,n = S.split()
            n = int(n)
            B = A.split("_")[1]
            self.push(n,B)
        elif "pop" in S:
            A,B = S.split("_")
            self.pop(B)
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
        if len(self.dequ) == 0:
            return 1
        else:
            return 0
    
    def push(self,n,B):
        if B == "front":
            self.dequ.appendleft(n)
        else:
            self.dequ.append(n)
        return None
    def pop(self,A):
        if self.isEmpty():
            print(-1)
        elif A == "front":
            a = self.dequ.popleft()
            print(a)
        else:
            a = self.dequ.pop()
            print(a)
        return None
    def size(self):
        print(len(self.dequ))
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
            print(self.dequ[0])
        return None
    def back(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.dequ[-1])
        return None

deq = dequ()
for _ in range(N):
    S = input().rstrip()
    deq.do(S)