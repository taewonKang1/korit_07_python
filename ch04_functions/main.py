# 매개 변수 x / 리턴 x
def call1():
    print('[ x | x ]')

# 매개변수 o / 리턴 x
def call2(unknown_parameter):
    print('[ o | x ]')
    print(f'{unknown_parameter} 라고 입력하셨다보네요')


# 매개변수 x | 리턴 o
def call3():
    print('[ x | o ]')
    return 1

def call4(unknown1, unknown2):
    print('[ o | o ]')
    return unknown1 + unknown2

call1()
call2('오늘의 날씨는 시원한 편')
call3()
print(call3())



'''
700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1~call4 중 어떤 유형일지 고민할 필요가 있습니다)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구성
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''

def vending_machine(money):
    price = 700
    max_drinks = money // price

    for drinks in range(max_drinks + 1):
        change = money - (drinks * price)
        print(f"음료수 = {drinks}개, 잔돈 = {change}원")


vending_machine(3000)

'''
예제 : 구구단 출력하기
함수 정의 :
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 :
multiply(dan)       #argument가 dan

실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3

...
3 x 9 = 27
'''

def multiply(dan):
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')

dan = int(input('몇 단을 출력하시겠습니까? >>> '))
multiply(dan)

'''
range() 함수의 parameter  적용 순서
1 개만 있을 때 : 한계값
2 개 있을 때 : 시작값, 한계값
3 개 있을 때 : 시작값, 한계값, 증감값 순서입니다.

그럼 현재 multiply를 call2() 유형으로 정의했다고 볼 수 있겠습니다.

call1() 유형으로 정의했을 때

실행 예
몇 단을 출력하시겠습니까? >>> 5
5 x 1 = 5
...
5 x 9 = 45
로 나올 수 있도록 작성하시오.
'''
def multiply2():
    num = int(input('몇 단을 출력하시겠습니까? >>> '))
    for i in range(1, 10):
        print(f'{num} x {i} = {num * i}')

multiply2()