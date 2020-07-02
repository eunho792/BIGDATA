#age = int(input("몇살이니"))
age =20
if age <19:
    print("아기")
else:
    print("성인입니다")

#a = int(input("숫자입력"))
a=3
if a ==3:
    print("3이다")
if a>5:
    print("5보다 크다")
if a<5:
    print("5보다 작다")

country= "Korea"
if country =="Korea":
    print("한국입니다")
if country=="korea":
        print("한국아닙니다")

a=3
if a>1 and a<10:
    print("OK")

a = 3
if 1<a < 10:
    print("ok")

age =22
if age<19:
    print("어서오세요")
elif age<25:
    print("대학생입니다")
else:
    print("가라")

age = 23
if age <19:
        print("애들은 가라")
else:
    if age <25:
        print("대학생입니다")
    else:
        print("어서오세요")

money = 6500
if money >=20000:
    print("탕수육을 먹는다")
else:
    if money >= 10000:print("쟁반 짜증을 먹는다")
if money >= 6000:
    print("짬뽕을 먹는다")
if money >= 4000:
    print("짜장면 먹는다")
else:
    print("단무지만 먹는다")

man = "true"
age = 22

if man=="true":
    if age>=19:
        print("성인ㄴ")
    else:
        print("소년")
else:
    print("ㅎ")

student = 1
while student <= 5:
        print(student, "번 한생의 성적을 처리한다")
        student +=1
sum = 0
for n in range(1,101):
    sum+=n
print(sum)

sum=0
for n in range(2,101,2):
    sum+=n
print(sum)

for x in range(1,51):
    if(x%10):print("+", end='')
    else: print("-", end='')
print(x)
n = 1
while n <=50:
    if (n%10):print("+",end='')
    else:print("-",end='')
    n=n+1
print(n)



for n in range(1,51):
    if(n%10):print("-",end='')

    else:print("+",end='')

def Stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

    while stack :
        print("POP Value is ", stack.pop())
        print(Stack())

