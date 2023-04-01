#####
def solution(n):
    first,last = -1,-1 # 첫번째 1, 마지막 1의 index를 저장
    k = n
    i = 0 # index 임시 저장용
    while True:
        if k%2 == 1 and first == -1:
            first = i
        elif k%2 == 0 and first > -1 and last == -1:
            last = i-1
        elif k == 0:
            if last == -1:
                last = i-1
            break
        else:
            k = k//2
            i += 1
    
    n += 2**(first) + ( 2**(last-first) -1)
    
    return n


### bin 함수 이용
#####
def solution(n):
    first,last = -1,-1 # 첫번째 1, 마지막 1의 index를 저장
    k = n
    i = 0 # index 임시 저장용
    count_1 = bin(n).count('1')
    
    n += 2**(first) + ( 2**(last-first) -1)
    
    return n