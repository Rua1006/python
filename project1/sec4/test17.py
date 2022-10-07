# 클래스(Class) : 객체를 만들기 위한 기본틀
# 함수(Function) : 기능을 위한 명령어들의 모임으로 어떤 클래스의 멤버가 아님
# 메소드(Method) : 클래스의 멤버로 기능을 위한 명령어들의 모임

def fnc1():                             #함수 : 독립적인 존재
    print("함수")
    
class test:
    x = y = 0                           #멤버 변수
    def __init__(self, a, b):           #생성자
        self.x=a
        self.y=b

    def plus(self):                     #멤버 메소드
        return self.x+self.y

    def minus(self):                    #멤버 메소드 : 함수와 동일하나 클래스에 속한 것
        return self.x-self.y

    def __del__(self):                  #소멸자(java는 finalize)
        print("객체가 소멸합니다")

fnc1()                                  #함수 호출
obj1 = test(20,40)                      #객체 생성
print("더한 결과 : ",obj1.plus())
print("뺀 결과 : ",obj1.minus())         #메소드 호출
del obj1                                #객체 소멸