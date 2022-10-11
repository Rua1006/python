# 입금, 출금, 잔액 조회가 가능한 은행 계좌관리 프로그램을 작성하여라
# 잔액(balance), 입출금액(money), 계좌번호(idNum),계좌주(idName)
# 입금기능(deposit), 출금기능(withdraw), 잔액조회(getBalance)
# 클래스의 멤버를 선언하여 작동될 수 있도록 할 것.

class Account:
    balance = 0
    def creatAccount(self, idNum, idName):
        self.idNum = idNum
        self.idName = idName
        self.balance = 0

    def deposit(self, money):
        self.balance+=money

    def withdraw(self, money):
        self.balance-=money


    def getBalance(self):
        return self.balance

account = Account()
account.creatAccount("7777","강병수")
account.deposit(1000000000)
account.withdraw(777777)
balance = account.getBalance()
print("계좌번호 :",account.idNum,"\n계좌주 : ",account.idName,"\n잔고 : ", balance)