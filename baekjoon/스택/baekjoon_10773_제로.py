import sys
input = sys.stdin.readline

K = int(input())

class moneystack():
    
    def __init__(self):
        self.moneystack = [0]
    
    def do(self,n):
        if n == 0:
            self.pop()
        else:
            self.push(n)
        return 0
    
    def pop(self):
        self.moneystack.pop()
        return 0
    
    def push(self, n):
        self.moneystack.append(n)
        return 0
    
    def summa(self):
        return sum(self.moneystack)

money = moneystack()

for _ in range(K):
    n = int(input())
    money.do(n)

print(money.summa())