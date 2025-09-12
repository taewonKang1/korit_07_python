from turtle import Turtle, Screen
from random import Random
# turtle 모듈에서 Turtle, Screen 클래스를 import 해왔습니다.

t = Turtle()        # 터틀 객체를 생성했고,  객체명 t
screen = Screen()   # 스크린 객체 생성
# 이상의 경우만 작성했을 때 모니터가 깜빡이는 것을 확인할 수 있는데, 이는 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것입니다.

t.shape('turtle')
t.color('white')
screen.bgcolor('black')

random = Random()
colors = [
    'dark red',
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow',
]

# for _ in range(10):
#     t.forward(20)
#     t.penup()
#     t.forward(20)
#     t.pendown()

# for _ in range(3):
#     t.forward(100)
#     t.left(120)
#
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
#
# for _ in range(6):
#     t.forward(100)
#     t.left(60)


# for i in range(3, 11):
#     for _ in range(i):
#         t.forward(100)
#         t.left(360/i)
#     t.color(random.choice(colors))

# 근데 도형 그릴 때마다 반복문 쓰는거 너무 짜증나니까 그냥 함수를 정의합시다
# def draw_shape(n):
#     for _ in range(n):
#         t.forward(100)
#         t.left(360/n)
#     t.color(random.choice(colors))
#
# def draw_dotted_line():
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#
# def draw_dotted_shape(n):
#     for _ in range(n):
#         draw_dotted_line()
#         t.left(360/n)
#     t.color(random.choice(colors))

# for i in range(3, 11):
#     draw_shape(i)

# for i in range(3, 11):
#     draw_dotted_shape(i)


# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# print(t.heading())

# .heading()의 return 값은 float
# .setheading()의 parameter가 float / return None

# t.setheading(t.heading() + 100)

# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)

t.speed(0)
# for _ in range(36):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 10)

# for _ in range(10):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 36)

# 함수화를 위한 일반식을 main에 작성하겠습니다.
# n = 10
# for _ in range(n):
#     t.color(random.choice(colors))
#     t.circle(100)
#     t.setheading(t.heading() + 360 / n)

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        t.color(random.choice(colors))
        t.circle(100)
        t.setheading(t.heading() + (360 / size_of_gap))

draw_spirograph(360)
# 이상의 코드에서의 문제점은
# 1. 매개변수인 size_of_gap은 n 번째 원과 n+1 번째 원의 각도 차이를 나타내는 것 같은데,
#    실제로는 반복횟수를 통제하고 있습니다.
# 2. 이상의 상황에서 나타내는 점은 360을 입력했을 때, 제자리에서 원이 생성 되는 것이 아니라,
#


screen.exitonclick()