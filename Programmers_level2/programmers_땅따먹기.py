def solution(land):
    last_line_num = [5]
    sum = [0]
    for j in land:
        A = []
        B = []
        for i in range(4):
            for k in range(len(sum)):
                if last_line_num[k] != i:
                    A.append(sum[k]+j[i])
                    B.append(i)
        last_line_num = B
        sum = A
        #print(sum, last_line_num)
    answer = max(sum)

    return answer

### 시간초과

