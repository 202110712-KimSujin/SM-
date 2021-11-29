import turtle as t
import winsound
import time
import random

#기본 설정(배경 및 제목)
t.title("파이썬 어렵조 - 달려라 거북이!")  
t.bgcolor("#f5f5dc")  
t.up()
t.ht()  
t.speed(0)
t.goto(0,240)
t.write("달려라 거북이!", False, "center", ("여기어때 잘난체",65))  # 글꼴 추가

#이미지호출
screen = t.Screen()
turtl = "거북이.gif"  # 이미지 추가
screen.addshape(turtl)
ttt = t.Turtle()
ttt.shape(turtl)

# 참가인원 받기
user_count = int(t.textinput("참가 인원을 입력하세요", "2명 이상의 플레이어가 참여 할 수 있습니다."))
ttt.ht()
t.clear()
screen.screensize(400,100 + (user_count*130))  #스크롤 만들기

# 게임 START 알림화면
t.goto(0,0)
t.pencolor("red")
t.write("START!", False, "center", ("여기어때 잘난체",60))  # 글꼴 추가
time.sleep(3)
t.clear()

#레이스 경기장 그리기
t.goto(0,240)
t.pencolor("black")
t.write("달려라 거북이!", False, "center", ("여기어때 잘난체",65))  # 글꼴 추가
t.goto(-400, 170)
t.down()
t.color("#a0522d")
t.begin_fill()
for i in range(2) :
    t.forward(800)
    t.right(90)
    t.forward((60 * user_count) - 20)
    t.right(90)
t.end_fill()

#결승선 그리기
t.color("red")  
t.pensize(3)  
t.up()
t.goto(330, 195)  
t.down()
t.delay(0)
for i in range (user_count*4):  # 점선 그리기 Code 추가
    t.setheading(270)
    t.forward(10)
    t.up()
    t.forward(5)
    t.down()
for i in range (2):   # 점선 모자라서 2개 더 추가하는 CODE
    t.setheading(270)
    t.forward(10)
    t.up()
    t.forward(5)
    t.down()
t.delay(10)

# 레이스 라인 생성
start_ycor_point = 150
start_ycor = list(range(user_count))
for i in range(user_count):
    start_ycor[i] = start_ycor_point - (i * 60)  # 라인 간격 60
    
for i in range(user_count-1):
    t.color("white")
    t.up()
    t.goto(-400, start_ycor[i] - 30)
    t.down()
    t.goto(400, start_ycor[i] - 30)

# 터틀 선수 생성
color_list= ["white", "red", "green", "yellow", "hotpink", "purple", "blue"]  # 각 터틀의 색 지정 

turtles= []  # 생성되는 터틀을 turtles 리스트에 넣음
for i in range(user_count):  # 입력한 수 만큼 터틀 생성
    new_turtle= t.Turtle()  # 객체생성
    new_turtle.up()
    new_turtle.shape("turtle")
    new_turtle.color(color_list[i % 7])  # Color 리스트 길이를 벗어나는 경우 modulo 연산자를 사용하여 반복시켜 준다
    new_turtle.goto(-370, start_ycor[i])  # 각 터틀선수의 번호 생성
    new_turtle.write(i+1)  # 0번이 아닌 1번부터 시작하고 싶어서 +1 했음
    new_turtle.goto(-350, start_ycor[i])  # 출발선에 있는 터틀 위치 (x,y)
    turtles.append(new_turtle)  # turtles 리스트에 생성된 터틀을 넣었음

#경기 시작 알림
winsound.Beep(523, 300)
time.sleep(0.3)

#경기 시작
game_over = False
while not game_over:
    # 도착점 이상의 거리를 가지게 되는 거북이가 생길 때 까지 반복
    for i in turtles:
        rand_distance = random.randint(1,10)
        i.forward(rand_distance)
        if i.xcor() > 310:
            game_over = True
            
# 1등 찾기
max_xcor = 0
winner = 0
for i in range(len(turtles)):
    # 최대 거리를 가지는 거북이 찾기
    if turtles[i].xcor() > max_xcor:
        max_xcor = turtles[i].xcor()
        winner = i+1
    #     print("Change = " + str(i) + " = " + str(max_xcor))
    # else:
    #     print("Not    = " + str(i) + " = " + str(max_xcor))
        
# 게임 결과 발표하기
t.up()
t.goto(0, 0)
t.down()
t.pencolor("#0000ff")
t.write(f"{winner}번 거북이의 승리!!", False, "center", ("여기어때 잘난체", 50))
t.done()
