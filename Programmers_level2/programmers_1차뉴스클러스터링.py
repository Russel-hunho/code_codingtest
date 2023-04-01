str1 = "aa1+aa2"
str2 = "AAAA12"
# 입력으로 들어온 문자열은
# 두 글자씩 끊어서 다중집합의 원소로 만든다.
# 대문자와 소문자의 차이는 무시한다.
# "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
# 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다
# 예를 들어 "ab+"가 입력으로 들어오면,
# "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list, str2_list = [],[]
    for i in range(len(str1)):
        if i+1 == len(str1):
            break
        if str1[i].islower() and str1[i+1].islower():
            str1_list.append(str1[i:i+2])
    for i in range(len(str2)):
        if i+1 == len(str2):
            break
        if str2[i].islower() and str2[i+1].islower():
            str2_list.append(str2[i:i+2])
    
    n1 = 0 #n1: 교집합 원소 수
    n2 = len(str1_list) + len(str2_list) #n2: 합집합 원소 수

    while True:
        if str1_list == []:
            break
        if str1_list[0] in str2_list:
            n1 += 1
            str2_list.remove(str1_list[0])
            str1_list.pop(0)
        else:
            str1_list.pop(0)
    n2 -= n1
    
    if n2 == 0:
        return 65536
    answer = n1 / n2
    return int(answer*65536)

# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

print(solution(str1,str2))