n = 437674
k = 3

n = 110011
k = 10

def solution(n, k):
    s = []
    while True:
        if n == 0:
            break
        else:
            s.insert(0,str(n%k))
            n //= k
    numlist_str = list(map(str,"".join(s).split("0")))
    numlist = [int(i) for i in numlist_str if i != ""]
    
    answer = 0
    for i in (set(numlist)-{1}):
        a = 0
        for j in range(2,int(i**(0.5))+1):
            if i%j == 0:
                a = 1
                break
        if a == 0:
            answer += numlist.count(i)
    return answer

print(solution(n,k))