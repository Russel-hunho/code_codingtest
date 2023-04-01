##https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 41:30

# N이 입력되면
# 00시00분00초부터 N시59분59초까지의 모든 시각 중
# 3이 하나라도 포함되는 모든 경우의 수 출력

N = int(input())
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            s = str(i)+str(j)+str(k)
            if "3" in s:
                count += 1
print(count)