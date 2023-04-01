import sys
lis = []
while True:
    S = sys.stdin.readline()
    if S == "":
        break
    else:
        lis.append(S)
for i in lis:
    print(i, end="")
    
## 핵심: EOF (End of File)을 잘 처리할 수 있는가
## 그냥 input으로 읽으면, 마지막 입력이 없는 상황에서 계속 기다린다!
## readline으로 읽는 경우, String에는 마지막 개행문자(\n)까지 저장된다! -> 출력시 자동으로 한줄 띄어짐
