id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

def solution(id_pw, db):
    if id_pw in db:
        return "login"
    elif id_pw[0] in list(zip(*db))[0]:
        return "wrong pw" 
    else:
        return "fail"
    
print(solution(id_pw,db))