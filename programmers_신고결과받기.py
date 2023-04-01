from pydoc import doc


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    report = list(set(report)) # 중복신고 제거
    reporting_id = [] #신고한사람
    reported_id = [] #신고당한사람
    counting_id = [0]*len(id_list) #신고받은횟수 count, id_list순
    getting_message_count = [0]*len(id_list) #report 받은 횟수 count, id_list순
    for i in range(len(report)):
        A,B = map(str,report[i].split(" "))
        reporting_id.append(A)
        reported_id.append(B)
        reported_index = id_list.index(B)
        counting_id[reported_index] += 1
    for j in range(len(id_list)):
        if counting_id[j] >= k:
            banned_id = id_list[j] #정지할 id
            for l in range(len(report)):
                if reported_id[l] == banned_id: #l번째 놈이 정지를 당한놈이라면
                    getting_message_count[id_list.index(reporting_id[l])] += 1 #l번째 신고한 놈의 count up
                    
    return getting_message_count


print(solution(id_list, report, k))

#####위에 시간초과남.. 줄여보기

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    report = list(set(report)) # 중복신고 제거
    reporting_id = [] #신고한사람
    reported_id = [] #신고당한사람
    counting_id = [0]*len(id_list) #신고받은횟수 count, id_list순
    getting_message_count = [0]*len(id_list) #report 받은 횟수 count, id_list순
    for i in range(len(report)):
        A,B = map(str,report[i].split(" "))
        reporting_id.append(A)
        reported_id.append(B)
        reported_index = id_list.index(B)
        counting_id[reported_index] += 1
    banned_id_list = [id_list[x] for x in range(len(id_list)) if counting_id[x] >= k]
    for j in range(len(report)):
        if reported_id[j] in banned_id_list:
            indexloc = id_list.index(reporting_id[j])
            getting_message_count[indexloc] += 1
    return getting_message_count


print(solution(id_list, report, k))


#####dictionary 활용

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    report = list(set(report)) # 중복신고 제거
    getting_message_count = [0]*len(id_list) #정지 report 받은 횟수 count, id_list순
    counting_dict = {x : 0 for x in id_list} #신고 받은 횟수
    
    for i in report:
        counting_dict[i.split()[1]] += 1
    #print(counting_dict)
    
    for i in report:
        if counting_dict[i.split()[1]] >= k:
            getting_message_count[id_list.index(i.split()[0])] += 1
    s
    return getting_message_count

print(solution(id_list, report, k))
