# 3개의 단어를 입력받아 첫 글자만 추출하여 약자를 출력하는 프로그램
# 반복문과 입력/출력/슬라이싱문 이용
# 입력예시
# 첫번째 단어 : Korea
# 두번째 단어 : Baseball
# 세번째 단어 : Organization
# 출력예시
# KBO

KBO=str(input())
print("KBO",KBO)

for(Korea, Baseball, Organiztion) in KBO:
    def kbo():
        a = int(input("첫번째 단어 : "))
        b = int(input("두번째 단어 : "))
        c = int(input("세번째 단어 : "))
        return a + b + c
print(kbo)