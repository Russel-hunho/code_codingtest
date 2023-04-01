import sys
input = sys.stdin.readline

T = int(input())

class isVPS():
    def __init__(self):
        self.isVPS = 0
    
    def do(self, S):
        if self.isVPS == 0 and len(S) == 0:
            print("YES")
        elif self.isVPS < 0 or len(S) == 0:
            print("NO")
        else:
            self.check(S)
        return 0
    
    def check(self, S):
        A = S.pop()
        if A == ")":
            self.isVPS += 1
        elif A == "(":
            self.isVPS -= 1
        return self.do(S)

for _ in range(T):
    N = isVPS()
    PS = list(input().rstrip())
    N.do(PS)