##https://www.youtube.com/watch?v=2zjoKjt97vQ&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=2&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98
# 18:55

#모든 연산은 왼쪽에서부터 진행
#각 자리는 0~9로만 이루어짐

Slist = list(int(i) for i in list(input()))
N = len(Slist)

tot = Slist[0]

for i in range(1,N):
    if tot in [0,1] or Slist[i] in [0,1]:
        tot += Slist[i]
    else:
        tot *= Slist[i]
print(tot)