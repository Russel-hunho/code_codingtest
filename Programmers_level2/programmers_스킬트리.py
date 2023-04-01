skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        A = [j for j in list(i) if j in list(skill)]
        if (skill[0] in A and "".join(A) in skill) or A == []:
            answer += 1
    return answer

print(solution(skill, skill_trees))