import turtle as t                                                  #거북이를 만들었어요
import random                                                       #이 코딩에서는 랜덤을 이용할거에요
t.shape ("circle")                                                  #모양은 동그라미 공으로
t.up()                                                              #펜 꼬리들고
t.goto(-250,-250)                                                   #x=-250 y=-250 좌표로 이동
t.down()                                                            #펜 꼬리 내리구
t.speed(0)                                                          #제일빠르게
def ground(n):                                                      #함수를 만들었어요
    for x in range(n):                                              #이 함수는 500x500 그라운드를 위한 거에요
        t.fd(500)                                                   #앞으로 500만큼
        t.lt(90)                                                    #왼쪽으로 90돌구

ground(4)                                                           #그렇게 n=4 를 입력하면 그라운드를 만듭니다.
t.up()                                                              #펜 꼬리 들고
t.home()                                                            #원래 위치로


a=random.randint(0,360)                                             #0~360의 값을 랜덤으로 정해요
t.setheading(a)                                                     #a도로 거북이 머리를 돌려요

while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :            #벽에 부딛힐 때까지 걸어갈거에요
    t.fd(1)                                                         #1만큼씩 걸어갈거에요


    
while True:                                                         #무한반복!
    ang = t.heading()                                               #현재 거북이의 각도를  ang에 저장해요
    
    if 0<= ang<= 45 or 135 <= ang <= 180:                           #만약 0~45 or 135~180 각도 안에 ang이 존재 하는 경우
        if -250<= t.xcor() <=250:                                   #첫번째를 제외 하구 n번째에는
            t.setheading(540-ang)                                   #360-ang 로 튕겨줘야해요
            t.fd(1)                                                 #1앞으로 걸어가구
            while -250<= t.xcor() <=250  and -250<= t.ycor() <=250: #벽에 부딛힐 때까지 걸어갈거에요
                t.fd(1)                                             #1만큼씩 걸어가요
        else:                                                       #그외에는
            t.setheading(180-ang)                                   #머리를 180-ang 만큼 돌려서
            t.fd(1)                                                 #한발자국 앞으로 (왜냐하면 while문을 이용해서 앞으로 걸어가기위해서는 250좌표에서 벗어나야 하기 때문입니다.)
            while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :#벽에 부딛힐 때까지 걸어갈거에요
                t.fd(1)                                             #1만큼씩 걸어가요

    if 45<= ang <=135 or 225 <= ang <= 315:                         #45~135 or 225~315 각도 안에 ang이 존재한다면
        if -250<= t.xcor() <=250:                                   #첫번째를 제외 하구 n번째에는
            t. setheading(540-ang)                                  #360-ang 로 튕겨줘야해요
            t.fd(1)                                                 #1앞으로 걸어가구
            while -250<= t.xcor() <=250  and -250<= t.ycor() <=250: #벽에 부딛힐 때까지 걸어갈거에요
                t.fd(1)                                             #1만큼씩 걸어가요
        else:                                                       #그 외에는
            t.setheading(360-ang)                                   #머리를 360-ang 만틈 돌려서
            t.fd(1)                                                 #한발자국 앞으로
            while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :#벽에 부딛힐 때까지 걸어갈거에요
                t.fd(1)                                             #1만큼씩요

    if 180<= ang <= 225 or 315 <= ang <= 360:                       #180~225 or 315~360 각도안에 ang 이 존재한다면
        if -250<= t.xcor() <=250:                                   #첫번째를 제외 하구 n번째에는
            t. setheading(540-ang)                                  #360-ang 로 튕겨줘야해요
            t.fd(1)                                                 #1앞으로 걸어가구
            while -250<= t.xcor() <=250  and -250<= t.ycor() <=250: #벽에 부딛힐 때까지 걸어갈거에요
                t.fd(1)                                             #1만큼씩 걸어가요
        else:                                                       #그외에는
            t.setheading(540-ang)                                   #머리를 540-ang 만큼 돌려서
            t.fd(1)                                                 #한발자국 걸어가요
            while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :#벽에 부딛힐 때까지 걸어갈거에요
                t.fd(1)                                             #1만큼씩 걸어가요

    if a == 0 or a == 45 or a== 90 or a==135 or a==180 or a==225 or a==270 or a==315 or a==360 :#a가 딱 0,45,90,135,180,225,270,315,360일때에는
        t.lt(180)                                                   #180도 돌거에요
        t.fd(1)                                                     #한발자국 걸어가구
        while -250<= t.xcor() <=250  and -250<= t.ycor() <=250 :    #벽에 부딛힐 때까지 걸어갈거에요
            t.fd(1)                                                 #1만큼씩 가요
