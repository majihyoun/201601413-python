x = input("비밀번호=")  #답을 x에 저장할거에요
a = int(x)              #x에 저장된 문자열을 정수로 바꿔줄거에요

if a == 480+6:
    print("정답!")      #답을 맞춘다면 정답!
    m = 5
    for x in range (m):
        import turtle as t
        t.shape("turtle")   #거북이의 축하를 보여줄거에요 별 다섯개!
        t.color("yellow")
        n = 5
        t.begin_fill()
        for x in range (n):
            t.fd(100)
            t.lt(144)
        t.end_fill()
        t.up()
        t.fd(100)
        t.down()
    t.reset()
    t.color("salmon")
    for x in range(200):
        t.lt(144)
        t.fd(x)
        t.speed(0)

        
else:
    print("땡ㅜㅜ")     #답을 틀린다면 땡ㅜㅜ
    import turtle as t  #틀린다면 동그라미의 저주에 걸린 거북이의 악몽을 보여줄거에요
    import random       
    t.shape("turtle")
    t.color("red")
    for x in range (1000):
         m = random.randint(1,360)
         t.setheading(m)
         t.circle(m)
         t.speed(0)
    t.reset()
    for x in range (50):
        t.circle(x)
