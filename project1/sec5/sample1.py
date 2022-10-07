#지방, 탄수화물, 단백질의 그램을 키보드로 입력하면 칼로리를
#계산하여 출력하는 프로그램
#총 칼로리 = 지방*9+단백질*4+탄수화물*4
#총 칼로리(calorie), 단백질(protein), 지방(fat), 탄수화물(carbohydrate)으로 변수 선언

class calcCalorie:


    def __init__(self, protein, fat, carbohydrate):
        self.protein = protein
        self.fat = fat
        self.carbohydrate = carbohydrate

    def calorie(self):
        calorie=self.fat*9+self.protein*4+self.carbohydrate*4
        return calorie

    int(input("지방 : ",fat,"탄수화물 :",carbohydrate,"단백질 : ",protein))

