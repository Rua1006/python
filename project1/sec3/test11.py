# 자료 구조 : 기본형(int, float, bool, str), 열거형(list, set, tuple, dict)
lst = [60, 70, 50, 90, 70, 80]  # list
tp = (60, 70, 50, 90, 70, 80)   # tuple 중간에 요소를 추가하거나 제거할 수 없음(읽기 전용)
st = {60, 70, 50, 90, 70, 80}   # set 중복을 허용하지 않음, 순서유지가 되지 않음(인덱스가 없다)
dct = {'kor':60, 'eng':70, 'mat':50, 'sci':90, 'his':70, 'art':80}  #dict(dictionary)
#dict는 key(항목이름)과 그에 해당하는 값으로 구성된다.

print("리스트 : ",type(lst), lst)
print("튜플 : ",type(tp), tp)
print("셋 : ",type(st), st)
print("딕트 : ",type(dct), dct)