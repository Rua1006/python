# 입금, 출금, 잔액 조회가 가능한 은행 계좌관리 프로그램을 작성하여라
# 잔액(balance), 입출금액(money), 계좌번호(idNum),계좌주(idName)
# 입금기능(deposit), 출금기능(withdraw), 잔액조회(getBalance)
# 클래스의 멤버를 선언하여 작동될 수 있도록 할 것.

class bank:

    def __int__(self, balance, money, idNum, idName):
        self.balance = balance
        self.money = money
        self.idNum = idNum
        self.idName = idName
    print()

    def add(self):
        balance = self.balance+self.money
        return balance

    def minus(self):
        balance = self.balance-self.money
        return balance

    def balance(self):
        balance = self.balance()
        return balance

    print("1-입금")
    print("2-출금")
    print("3-잔액조회")

    num = input("작업번호 선택 1/2/3")
    num1 = int(input("입금"))
    num2 = int(input("출금"))
    num3 = int(input("잔액조회"))

while True:
    if num1 == '1':
        print(num1,add())
    elif num2 == '2':
        print(num2,minus())
    elif num3 == '3':
        print(num3,balance())
    else:
        print("작업종료")