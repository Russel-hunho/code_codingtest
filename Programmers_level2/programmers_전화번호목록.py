phone_book = ["119", "97674223", "1195524421"]
phone_book =["12","123","1235","567","88"]

def solution(phone_book):
    phone_book.sort(key = len)
    
    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][0:l]:
                return False
    return True

print(solution(phone_book))


## 효율성 Test 실패...

phone_book =["12","123","1235","567","88"]

def solution(phone_book):
    phone_book.sort(key = len)
    
    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            n = 0
            for k in range(l):
                if n != 0:
                    break
                if phone_book[i][k] != phone_book[j][k]:
                    n = 1
            if k == l-1 and n == 0:
                return False
    return True

print(solution(phone_book))

## 더 느려짐..

phone_book = ["119", "97674223", "1195524421"]
phone_book =["12","123","1235","567","88"]

def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if len(phone_book[j]) == l:
                break
            if phone_book[i] == phone_book[j][0:l]:
                return False
    return True

print(solution(phone_book))
