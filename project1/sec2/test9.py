# 반복문 : 해당 조건이나 상황이 만족 될 때 반복 수행
i=tot=0
while(i<=10):
    tot+=i      #tot=tot+i
    i+=1        #i=i+1
print("0~10 합계 : ", tot)

# 1~100 짝수의 합계
e=tot2=0
while(e<=100):
    tot2+=e
    e+=2
print("짝수의 합계1 : ", tot2)

# 무한 루프
i=tot=0
while True:
    if(i>100):
        break
    tot+=1
    i+=2
print("짝수의 합계2 : ", tot)

i=1
tot=0
while True:
    if(i>100):
        break
    tot+=1
    i+=2
print("홀수의 합계1 : ", tot)