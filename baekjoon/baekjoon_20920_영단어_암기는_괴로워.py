import sys
input = sys.stdin.readline
N,M = map(int,input().split())
wordsinput = []
wordsdict = dict()
for _ in range(N):
    s = input().rstrip()
    if len(s) >= M:
        wordsinput.append(s)
words = set(wordsinput)
for i in words:
    wordsdict[i] = 0
for i in wordsinput:
    wordsdict[i] += 1
A = sorted(wordsdict.items(), key = lambda x:(-x[1],-len(x[0]),x[0]))
for i in A:
    print(i[0])