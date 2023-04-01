number, limit, power = 5,3,2

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        if i == 1:
            count = 1
        elif i < 4:
            count = 2
        else: 
            count = 2
            for j in range(2,int( i**(0.5) )+1):
                if i%j == 0:
                    count = count + 2
                '''if count > limit:
                    count = power
                    break # j for문 밖으로'''
            if (int(i**0.5))**2 == i:
                count = count - 1
        if count > limit:
            count = power
        answer += count
    return answer

print(solution(number, limit, power))