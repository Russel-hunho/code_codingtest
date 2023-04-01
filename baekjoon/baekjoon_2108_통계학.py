import sys
N = int(sys.stdin.readline())
countinglist = [0]*8001 # 0~3999: -4000~-1, 4000: 0, 4001~8000: 1~4000
summa = 0
mini = 4000
maxi = -4000
for _ in range(N):
    k = int(sys.stdin.readline())
    countinglist[k+4000] += 1
    summa += k
    mini = min(mini,k)
    maxi = max(maxi,k)

#산술평균
print(round(summa/N))
#중앙값, 최빈값
countmiddle = 0
famous = 0 #최빈값의 빈도수
famouslist = [] #최빈값 모음
for i in range(8001):
    x = countinglist[i]
    if x > famous:
        famous = x
        famouslist = [i-4000]
    elif x == famous:
        famouslist.append(i-4000)
    if countmiddle <= N//2 and countmiddle + x >= N//2+1:
        print(i-4000)
    countmiddle += x
if len(famouslist) == 1:
    print(famouslist[0])
else:
    print(famouslist[1])
#범위
print(maxi-mini)