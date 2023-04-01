import sys
S = sys.stdin.readline().rstrip()
L = len(S)
tot = 0
for i in range(1,L+1):
    temp = []
    for j in range(L-i+1):
        temp.append(S[j:j+i])
    #print(set(temp))
    tot += len(set(temp))
print(tot)