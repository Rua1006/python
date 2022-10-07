import keyword
#예약어 출력
print(keyword.kwlist)

#출력 형식 : %s(문자열), %d(10진 정수), %o(8진수), %x(16진수), %c(한글자), %f(실수)

name = "gu gu gu"
age = 100
height = 182.8
weight = 75.1
print("이름 : %s, 나이 : %d, 키 : %.2f" %(name,age,height))
print("8진수 : %o\n" % age)
print("16진수 : %x\n" % age)
print("2진수 : %a\n" % bin(age)) #a=모든 출력 형식을 뜻함
print("이름 : {}, 나이 : {}, 키 : {}".format(name,age,height))