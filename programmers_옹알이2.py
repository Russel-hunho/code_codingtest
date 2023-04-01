babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

def solution(babbling):
    answer = 0
    joka_2 = ["ye","ma"]
    joka_3 = ["aya","woo"]
    for i in range(len(babbling)):
        bibap = "k"
        while True:
            if babbling[i] == "":
                answer += 1
                break
            elif len(babbling[i]) == 1:
                break
            elif len(babbling[i]) == 2:
                if (babbling[i] not in joka_2) or (babbling[i] == bibap):
                    break
                else:
                    answer += 1
                    break
            elif (babbling[i][0:2] in joka_2) and (babbling[i] != bibap):
                bibab = babbling[i][0:2]
                babbling[i] = babbling[i][2:]
            elif (babbling[i][0:3] in joka_3) and (babbling[i] != bibap):
                bibab = babbling[i][0:3]
                babbling[i] = babbling[i][3:]
            else:
                break
    return answer

print(solution(babbling))