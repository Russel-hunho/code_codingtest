import sys
input = sys.stdin.readline

N = int(input())

class stack():
    # 이 Class 안에서 호출할때는 self.stack으로 호출
    # 외부 정의 함수 사용시에는, self.stack.append()느낌
    # 내부 정의 함수 사용시에는, self.top() 느낌
    # 내부 함수 정의 시에는, "함수명(self, 함수에 사용될 변수들):" 형식
    # st = stack() 으로 정의 시,
    # st.top() 식으로 사용!

    # 최초 선언시 정의
    def __init__(self):
        self.stack = []
    
    # 문자열 S에 맞게 구문을 실행하라
    def do(self, S):
        if "push" in S:
            n = int(S.split()[1])
            self.push(n)
        elif "pop" == S:
            self.pop()
        elif "size" == S:
            self.size()
        elif "empty" == S:
            self.empty()
        else: #top
            self.top()
        return 0
    
    def push(self,data):
        self.stack.append(data)
        return 0
    
    def pop(self):
        if self.isEmpty():
            print(-1)
        else:
            #마지막 것 빼오기
            pop_object = self.stack.pop() # 이건 외부 함수 pop임!!
            print(pop_object)
        return 0
    
    def size(self):
        print(len(self.stack))
        return 0
    
    def empty(self):
        if self.isEmpty():
            print(1)
        else:
            print(0)
        return 0
    
    def top(self):
        if self.isEmpty():
            print(-1)
        else:
            print(self.stack[-1])
        return 0
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    
st = stack()
# __init__에 맞춰 생성된다. 즉 stack 자료형이면서, []가 st에 저장됨

for _ in range(N):
    instr = input().rstrip()
    st.do(instr)