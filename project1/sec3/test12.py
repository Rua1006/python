#리스트 : 요소를 선언, 추가, 삽입, 수정, 삭제, 정렬
#인덱스가 존재하여 순서 제어가 가능
a=[]    #빈 리스트
b=["kim", 1004, 6.28, True] #python은 각기 다른 데이터 타입을 저장가능
print(id(b), type(b), b)
print(id(b[0]), type(b[0]),b[0]) #변수명[인덱스] : 특정 번째 데이터정보 확인가능
print(b[1:3])   #인덱스가 1인 요소부터 2인 요소까지
print(b[1:])    #인덱스가 1인 요소부터 끝까지
print(b[:3])    #인덱스 처음부터 2인 요소까지
print(b[0:3:3]) #인덱스 2인요소까지 중 홀수번째만
print(b[::-1])  #인덱스 역순 정렬
b.append(18)    #b[4] = 18
print(b)
del b[1]        #b[1]이 제거되면서 뒤에 요소를 당겨옴
print(b)
b[3]=1004       #b[3]의 저장값을 1004로 변경
print(b)
b.insert(2, "Angel")    #b[2]의 원소를 삽입
print(b)
c=["kang", 100, "A", False]
d=b+c           #요소 합치기
print(d)
comment = "My name is Byungsu, Kang, Lee, Kim, Han"
e=comment.split(sep=' ')    #요소 분리
print(e)
print(e.index('Kang,'))  #특정 원소의 위치(인덱스) 찾기
print("개수 : ", e.count('Kang,'))    #특정 원소의 개수 구하기
print("전체 원소의 수 : ",len(e))      #전체 원소의 수
e=[90,40,100,70,60,80,50]
print("정렬 전 : ",e)
f=e.sort()                           #오름차순 정렬
print("오름차순 정렬 : ",e)
g=e.reverse()                        #내림차순 정렬
print("내림차순 정렬 : ",e)
#e.remove(2)                         #인덱스가 2인 원소 제거
e.pop()                              #스택(LIFO) pop 연산 = 가장 마지막 데이터 끌어내기 위해
print("pop 연산 후 :", e)
e.pop(1)                             #특정 인덱스 위치 원소를 끌어 내기
print("인덱스가 1인 pop 연산 후 :", e)
e.extend([90,80])
print("확장 후 : ", e)
help(list)