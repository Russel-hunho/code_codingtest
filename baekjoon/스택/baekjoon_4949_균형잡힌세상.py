import sys
input = sys.stdin.readline

class isBalanced():
    
    def __init__(self):
        self.isBalanced = []
        return None
    
    def do(self, S):
        if len(S) == 0 and self.isBalanced == []:
            print("yes")
        elif len(S) == 0 or self.isBa
            print("no")
        else:
            self.stack(S)
    
    def stack(self, S):
        A = None
        while not self.isEmpty(S):
            A = S.pop()
            if A in ["(",")","[","]"]:
                break
            A = None
        if A == None:
            수정
        elif A in [")","]"]:
            self.isBalanced.append(A)
        elif A == "(":
            if self.isBalanced[-1] == ")":
                self.isBalanced.pop()
            else:
                처리해
        elif A == "[":
            if self.isBalanced[-1] == ")":
                self.isBalanced.pop()
            else:
                처리해
            
    def isEmpty(self,S):
        if len(S) == 0:
            return 1
        else:
            return 0


while True:
    S = input().rstrip
    if S == ".":
        break
    S = list(S)
    N = isBalanced()
    N.do(S)