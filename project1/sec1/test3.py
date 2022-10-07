#연산 : 산술, 관계(비교), 논리, 대입 및 할당 연산, 증감연산, 비트 연산...
a=30
b=50
c=70
d=a+b
e=a-b
f=a*b
g=b/a
h=b%a   #나머지
i=b//a  #몫
j=b**3  #거듭제곱

print("a+b=",d)
print("a-b=",e)
print("a*b=",f)
print("b/a=",g)
print("b%a=",h)
print("b//a=",i)
print("b**3=",j)

# noinspection PyUnresolvedReferences
print("a=", a++) #출력 30, 실제 a=31 -> 후위연산
print("b=", ++b) #출력 51, 실제 b=51 -> 전위연산

a=20
b=30
# noinspection PyUnresolvedReferences
print("a=", a--) #출력 20, 실제 a=19
print("b=", --b) #출력 29, 실제 b=29

#대입(할당) 연산자
a=20
b=30
a+=3    #a가 3씩 증가
a-=3    #a가 3씩 감소
a*=3    #a가 3씩 누승
a/=3    #a가 3씩 누분
a%=3    #a값에 해당하는 값을 3으로 나눈 후에 다시 나머지 저장

b1=20
b2=40
print("b1=",b1)
print("b2=",b2)
b1,b2=b2,b1 #교환 연산
print("교환 후")
print("b1=",b1)
print("b2=",b2)
c1, *arr = {20,60,50,40,30} #할당 연산
print("c1=",c1)
print("arr=",arr)