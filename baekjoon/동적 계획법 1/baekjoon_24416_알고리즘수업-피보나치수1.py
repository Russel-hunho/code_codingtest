## 재귀 방법
# return으로 이전 값의 함수를 반복실행하도록
# 결국, 피보나치수만큼 반복계산해야된다.
'''
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
'''

## 동적계획법 방법
# F1~Fn을 계산하며 함수 안에 저장하여, n번만 실행되면 된다!
'''
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
'''

n = int(input())

def fibonachi(n):
    f = [0,1,1]
    for j in range(3,n+1):
        f.append( f[-1]+f[-2] )
    return f[n]

print("{} {}".format(fibonachi(n),n-2))