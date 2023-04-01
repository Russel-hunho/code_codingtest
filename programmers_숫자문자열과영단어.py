S = input()

def solution(s):
    alphabet = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    answer = 0
    
    i = 0
    while i < len(s):
        if ord(s[i]) < 60:      # 아스키 이용, 숫자인 경우
            answer = answer * 10 + int(s[i])
            i += 1
        else:
            for j in range(10):
                if alphabet[j] in s[i:i+5]:
                    answer = answer * 10 + j
                    i += len(alphabet[j])
                    break
    return answer

print(solution(S))

## dictionary 이용 훨씬 간단하게
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8","nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
