# 함수(function) 그리고 클래스(class)
def plus1():            # 매개변수 없고, 리턴도 없음
    print("더하기")

def plus2(a,b):         # 매개변수 있고, 리턴은 없음
    print(a+b)

def plus3():            # 매개변수 없고, 리턴 있음
    a=int(input("숫자1 : "))
    b=int(input("숫자2 : "))
    return a+b

def plus4(a,b):         # 매개변수 있고, 리턴 있음
    return a+b

plus1()                 # 매개변수X, 리턴X
a=int(input("숫자1 : "))
b=int(input("숫자2 : "))
plus2(a,b)              # 매개변수O, 리턴X
hap1 = plus3()          # 매개변수X, 리턴O
print(hap1)
hap2 = plus4(a,b)       # 매개변수O, 리턴O
print(hap2)

#호출 및 전달 방식
#call by value
#call by name
#call by reperense