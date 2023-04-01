genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    gen_type = dict() # {장르이름 : 총Play수}
    gen_dict = dict() # {장르이름 : {인덱스 : playtime} }  # 2차원 dict
    for i in range(len(genres)):
        if genres[i] in gen_type.keys():
            gen_type[genres[i]] += plays[i]
            gen_dict[genres[i]][i] = plays[i]
        else:
            gen_type[genres[i]] = plays[i]
            gen_dict[genres[i]] = {i:plays[i]}
    
    #장르별 play 시간 수대로 내림차순
    gen_type = dict(sorted(gen_type.items(), key = lambda x:x[1], reverse = True))
    answer = []
    for i in gen_type.keys():
        answer += list(dict(sorted(gen_dict[i].items(), key = lambda x:x[1], reverse = True)).keys())[0:2]
    
    return answer