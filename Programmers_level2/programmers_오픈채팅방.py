record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    ID_Name_dict = dict()
    Msg_list = []
    ID_list = []
    for i in record:
        A = list(map(str,i.split(" ")))
        [cord, id] = A[0:2]
        if cord == "Enter":
            Msg_list.append("님이 들어왔습니다.")
            ID_list.append(id)
            ID_Name_dict[id] = A[2]
                # Enter의 경우, ID의 Name이 무조건 바뀜
        elif cord == "Leave":
            Msg_list.append("님이 나갔습니다.")
            ID_list.append(id)
                # Leave의 경우 ID 바꾸는 행위는 없음
        else: #cord = change
            ID_Name_dict[id] = A[2]
    
    for j in range(len(Msg_list)):
        answer.append( ID_Name_dict[ID_list[j]] + Msg_list[j])
    
    return answer

print(solution(record))