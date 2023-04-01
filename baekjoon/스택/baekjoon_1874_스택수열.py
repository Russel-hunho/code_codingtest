import sys
input = sys.stdin.readline

n = int(input())

Astack = []
B = list(range(n+1,0,-1)) #1부터 n까지 차례로 빼내기 위함
Cstack = [] # +,- 저장용

state = 1
for _ in range(n):
    k = int(input())
    while True:
        if len(B) == 0:
            state = 0
            break
        if len(Astack) != 0:
            if k == Astack[-1]:
                Astack.pop()
                Cstack.append("-")
                break
            else:
                b = B.pop()
                #b를 Stack에 Push부터 한다.
                Astack.append(b)
                Cstack.append("+")
        else:
            b = B.pop()
            #b를 Stack에 Push부터 한다.
            Astack.append(b)
            Cstack.append("+")

if state == 1:
    for i in Cstack:
        print(i)
else:
    print("NO")