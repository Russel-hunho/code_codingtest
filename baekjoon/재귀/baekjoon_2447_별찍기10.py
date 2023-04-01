N = int(input())
#3의 거듭제곱으로만 주어짐

def f(N):
    if N == 3:
        return [["*","*","*"],["*"," ","*"],["*","*","*"]]
    else:
        temp = f(N//3)
        L = len(temp)
        A = []
        for i in range(L):
            A.append(temp[i]*3)
        for i in range(L):
            A.append(temp[i] + [" "]*L + temp[i])
        for i in range(L):
            A.append(temp[i]*3)
        return A

B = f(N)
for i in B:
    print("".join(i))