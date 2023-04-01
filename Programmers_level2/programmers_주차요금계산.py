fees = [180, 5000, 10, 600]
# 기본 시간(분)
# 기본 요금(원)	
# 단위 시간(분)	
# 단위 요금(원)

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


def solution(fees, records):
    answer = dict()
    inout_dict = dict() # number: in_time
    
    #요금계산함수
    def fee(intime,outtime):
        inH, inM = map(int,intime.split(":"))
        outH,outM = map(int,outtime.split(":"))
        del_time = (outH-inH)*60+(outM-inM)
        if del_time <= fees[0]:
            return fees[1]
        else:
            return fees[1] + ((del_time-fees[0]-1)//fees[2]+1)*fees[3]
    
    for i in records:
        time, number, inout = map(str,i.split(" "))
        if inout == "IN":
            inout_dict[number] = time
        else: # OUT
            intime = inout_dict[number]
            if number in answer.keys():
                answer[number] += fee(intime,time)
            else:
                answer[number] = fee(intime,time)
            print(answer)
            inout_dict[number] = "End"
    
    for j in inout_dict.keys():
        number = j
        if inout_dict[j] != "End":
            intime = inout_dict[j]
            if number in answer.keys():
                answer[number] += fee(intime,"23:59")
            else:
                answer[number] = fee(intime,"23:59")
    
    return answer

# 출차 기록 없으면
# 23:59에 출차된 것으로 간주

# 차량 번호가 작은 자동차부터
# 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

print(solution(fees, records))
#[14600, 34400, 5000]



##### 여러번 출입할경우,
# 초기화가 아니라, 최종 시간으로 계산해야됨..

fees = [180, 5000, 10, 600]
# 기본 시간(분)
# 기본 요금(원)	
# 단위 시간(분)	
# 단위 요금(원)

records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


def solution(fees, records):
    answer = []
    inout_dict = dict() # number: in_time
    del_time_dict = dict() # number: del_time
    
    #시간계산함수
    def del_time(intime,outtime):
        inH, inM = map(int,intime.split(":"))
        outH,outM = map(int,outtime.split(":"))
        return (outH-inH)*60+(outM-inM)
    
    #요금계산함수
    def fee(del_time):
        if del_time <= fees[0]:
            return fees[1]
        else:
            return fees[1] + ((del_time-fees[0]-1)//fees[2]+1)*fees[3]
    
    for i in records:
        time, number, inout = map(str,i.split(" "))
        if inout == "IN":
            inout_dict[number] = time
        else: # OUT
            intime = inout_dict[number]
            if number in del_time_dict.keys():
                del_time_dict[number] += del_time(intime,time)
            else:
                del_time_dict[number] = del_time(intime,time)
            print(del_time_dict)
            inout_dict[number] = "End"
    
    for j in inout_dict.keys():
        number = j
        if inout_dict[j] != "End":
            intime = inout_dict[j]
            if number in del_time_dict.keys():
                del_time_dict[number] += del_time(intime,"23:59")
            else:
                del_time_dict[number] = del_time(intime,"23:59")
    
    sorted_del_time_dict = dict(sorted(del_time_dict.items()))
    for j in sorted_del_time_dict.keys():
        answer.append(fee(sorted_del_time_dict[j]))
    
    return answer

# 출차 기록 없으면
# 23:59에 출차된 것으로 간주

# 차량 번호가 작은 자동차부터
# 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

print(solution(fees, records))
#[14600, 34400, 5000]