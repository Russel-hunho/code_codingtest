k,m = 4,3
#max: k점
# m개씩 한 상자로 묶어 포장
# 각 상자의 가격: 최저점수 * m개
# m개로 나눈 후 남은건 버림

score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

def solution(k, m, score):
    answer = 0
    l = len(score)%m # 그냥 버릴 사과 수
    score.sort()
    del score[0:l] #버리기 완료
    for i in range( len(score)//m ):
        answer += score[(i*m)] * m
    return answer

print(solution(k,m,score))