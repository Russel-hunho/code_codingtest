N = int(input())
state = 1
for i in range(1,N+1):
    if N == (i + i%10 + (i//10)%10 + (i//100)%10 + (i//1000)%10 + (i//10000)%10 + (i//100000)%10 + (i//1000000)%10):
        state = 0
        print(i)
        break
if state == 1:
    print(0)