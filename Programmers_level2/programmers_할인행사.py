want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-10+1):
        temp = discount[i:i+10]
        temp_num = []
        for j in want:
            temp_num.append(temp.count(j))
        if temp_num == number:
            answer += 1
    
    return answer
print(solution(want, number, discount))