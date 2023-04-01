N = input()
numlist = list(map(int,input().split()))
M = max(numlist)
#에라스토테네스의 체
primes = []
numstate = [False,False]+[True]*(M-1) #0부터M까지 #0,1은 false, 2부터 True로 설정해둠
for i in range(2,M+1):
    if numstate[i]:
        primes.append(i)
        for j in range(i*2,M+1,i):
            numstate[j] = False # i의 배수는 다 False로 만듬

Ans = 0
for k in numlist:
    if k in primes:
        Ans += 1
print(Ans)
