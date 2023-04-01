def solution(prices):
    answer = []
    for i in range(len(prices)):
        n = 0
        for j in range(i,len(prices)):
            if j == len(prices)-1:
                answer.append(n)
            elif prices[j] >= prices[i]:
                n += 1
            else:
                answer.append(n)
                break
    return answer

### 시간초과

prices = [1, 2, 3, 2, 3]

def solution(prices):
    A = [i for i in prices]
    A.sort()
    answer = []
    price_dict = dict()
    
    for i in range(len(prices)):
        price_dict[i] = A.index(prices[i])
    
    
    for price in prices:
        
    
    while True:
        prices[0]


print(solution(prices))