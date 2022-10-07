# 임의의 1~45 의 여섯 개 숫자를 출력하도록 하되, 중복이 허용되지 않는
# 로또 번호 발생 프로그램을 작성하라

import random

lotto = [0,0,0,0,0,0]
a = range(6)
for i in a:
    lotto[i]=random.randint(1,45)
    print(lotto[i])
setlotto = set(lotto)

i=0
while True:
    if(len(setlotto)<6):
        b =random.randint(1,45)
        setlotto.add(b)
    if(len(setlotto)==6):
        lotto=list(setlotto)
        lotto.sort()
        break
print("로또번호 :",lotto)