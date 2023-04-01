m = "ABCDEFG"
# 기억한 멜로디
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# 각각의 곡 정보를 담고있는 배열
# 시작시간, 끝시간, 곡제목, 곡의 음 진행(1분에한음씩,끝시간까지 반복)


# 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
# 조건이 일치하는 음악이 여러 개일 때에는
    # 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다.
    # 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.

def solution(m, musicinfos):
    musicdict = dict()
    for i in musicinfos:
        Streaming = ""
        start,end,name,melody = map(str,i.split(","))
        time = (int(end[0:2])-int(start[0:2]))*60 + (int(end[3:5])-int(start[3:5]))
        j = 0
        l = len(melody)
        for _ in range(time):
            Streaming += melody[j%l]
            if melody[(j+1)%l] == "#":
                j+=1
                Streaming += melody[j%l]
            j+=1
                
        
        if m in Streaming:
            if m[-1] == "#":
                musicdict[name] = time
            elif m + "#" not in Streaming:
                musicdict[name] = time
            else:
                Streaming = Streaming.replace(m + "#", " ")
                if m in Streaming:
                    musicdict[name] = time
    
    if musicdict == {}:
        return "(None)"
    return max(musicdict, key = musicdict.get)
    #Value 기준으로 max인 놈의 key를 str으로 반횐