numbers = "17"

from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    numbers.sort(reverse = True)
    maxnum = int("".join(numbers))
    
    def make_numberlist(numbers):
        numberlist = []
        for i in range(1,len(numbers)+1):
            A = list(map("".join,permutations(numbers,i)))
            for j in A:
                numberlist.append(int(j))
        numberlist = list(set(numberlist))
        return numberlist
    
    numberlist = make_numberlist(numbers)
    
    def make_primenum_list(num):
        TOT = set(range(2,num+1))
        i = 0
        while True:
            if i in TOT:
                TOT = TOT-set(range(2*i,(num//i+1)*i,i))
            i += 1
            if i >= num:
                break
        primenum_list = list(TOT)
        return primenum_list
    
    primenum_list = make_primenum_list(maxnum)
    
    X = [i for i in numberlist if i in primenum_list]
    
    return len(X)

print(solution(numbers))


###시간초과
##각 수를 소수판별해보자

numbers = "17"

from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    numbers.sort(reverse = True)
    maxnum = int("".join(numbers))
    
    def make_numberlist(numbers):
        numberlist = []
        for i in range(1,len(numbers)+1):
            A = list(map("".join,permutations(numbers,i)))
            for j in A:
                numberlist.append(int(j))
        numberlist = list(set(numberlist))
        return numberlist
    
    numberlist = make_numberlist(numbers)
    
    def isprimenum(num):
        if num < 2:
            return 0
        for i in range(2,int(num**0.5+1)):
            if num % i == 0:
                return 0
        return 1
    
    answer = 0
    for i in numberlist:
        answer += isprimenum(i)
    
    return answer

print(solution(numbers))