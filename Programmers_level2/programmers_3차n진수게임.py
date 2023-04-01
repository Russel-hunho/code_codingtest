n,t,m,p = 16,16,2,2
# 진법 n
# 미리 구할 숫자의 갯수 t
# 게임에 참가하는 인원 m
# 튜브의 순서 p

# 0부터 시작

def solution(n, t, m, p):
    answer = ""
    num = "0"
    temp_num = 1
    
    def temp_str(temp_num,n):
        s = []
        k = temp_num
        while True:
            if k == 0:
                break
            else:
                s.append(k%n)
                k //= n
        s.reverse()
        for i in range(len(s)):
            if s[i] >= 10:
                s[i] = chr( ord("A")+(s[i]-10) )
            else:
                s[i] = str(s[i])
        return "".join(s)
    
    while True:
        if len(num) >= m*t:
            break
        else:
            num += temp_str(temp_num,n)
            temp_num += 1
    
    #print(num)
    for i in range(t):
        answer += num[p+m*i-1]
        #print(answer,p+m*i)
    
    return answer


print(solution(n, t, m, p))