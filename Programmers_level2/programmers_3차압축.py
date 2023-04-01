msg = "KAKAO"

def solution(msg):
    #초기 색인번호: 
    Word = [chr(j) for j in range(ord("A"),ord("Z")+1)]
    Word_dict = {i: ord(i)-ord("A")+1 for i in Word}
    last_num = 26
    answer = []
    while True:
        i = 1
        k = 0
        while True:
            if msg[0:i] not in Word_dict.keys():
                last_num += 1
                Word_dict[msg[0:i]] = last_num
                answer.append(Word_dict[msg[0:i-1]]) #출력값 추가
                msg = msg[i-1:]
                break
            elif i == len(msg):
                answer.append(Word_dict[msg])
                k = 1
                break
            else:
                i += 1
        if k == 1:
            break
    return answer

print(solution(msg))