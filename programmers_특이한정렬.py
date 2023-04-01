def solution(numlist, n):
    gap_dict = {x:abs(x-n) for x in numlist}
    print(gap_dict)
    gaplist = [abs(i-n) for i in numlist]
    
    answer = []
    while True:
        numlist.remove
        answer
    
    gap = [i for i in gaplist]
    gaplist.sort()
    
    return answer



####

numlist = [10000,20,36,47,40,6,10,7000]
n=30

def solution(numlist, n):
    answer = [numlist[0]]
    gap = [numlist[0]-n]
    for i in numlist[1:]:
        j = 0
        while True:
            if j == len(answer):
                answer.insert(j,i)
                gap.insert(j,i-n)
                break
            elif abs(i-n) < abs(gap[j]):
                answer.insert(j,i)
                gap.insert(j,i-n)
                break
            elif abs(i-n) == abs(gap[j]):
                if i > n:
                    answer.insert(j,i)
                    gap.insert(j,i-n)
                    break
                else:
                    answer.insert(j+1,i)
                    gap.insert(j+1,i-n)
                    break
            else:
                j += 1
    return answer

print(solution(numlist,n))