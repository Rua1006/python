# 아래와 같이 회원에 대한 지역 데이터가 있다. 각 지역별 빈도수를 구하여 출력하라
# 서울, 부산, 경기, 대전, 서울, 광주, 대구, 서울, 부산, 인천,
# 서울, 대전, 경기, 서울, 경기

area = "서울, 부산, 경기, 대전, 서울, 광주, 대구, 서울, 부산, 인천, 서울, 대전, 경기, 서울, 경기"

print("지역별 빈도수 : ","서울(",area.count('서울,'),")","경기(",area.count('경기,'),")","인천(",area.count('인천,'),")"
      ,"대전(",area.count('대전,'),")","광주(",area.count('광주,'),")","대구(",area.count('대구,'),")"
      ,"부산(",area.count('부산,'),")")

data =["서울, 부산, 경기, 대전, 서울, 광주, 대구, 서울, 부산, 인천, 서울, 대전, 경기, 서울, 경기"]
region = set(data)
for key in region:
      cnt = 0
      for comp in data:
            if(comp==key):
                  cnt+=1
      print(key," : ",cnt)