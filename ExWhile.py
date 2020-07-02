treeHit = 0
while treeHit <10:
    treeHit +=1
    print("나무를 %d번 찍었습니다,"%treeHit)
    if treeHit ==10:
        print("나무 넘어갑니다")

prompt ="""
1. Add
2. Del
3. List
4. Quit

Enter number:"""


# number = 0
# while number !=4:
#     print(prompt)
#     number= int(input())

coffee = 10
money = 300
while money:
    print("돈을 받읐으니 커피를 줍니다")
    coffee -=1
    print("남은커피양은 %d 입니다"%coffee)
    if coffee==0:
        print("커피가 다 떨어졋습니다. 판매를 중지합니다")
        break


a = 0
while a< 10:
    a = a+1
    if a % 2 ==0: continue
    print(a,end=" ")

a = [(1,2), (3,4) , (5,6)]
for (first , last) in a:
    print(first+last)

marks = [90, 25 , 67, 45, 80]


for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생은 합격 입니다," % (number+1))

a = range(10)


add = 0
for i in range(1,11):
    add +=i
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end="    ")
    print("")

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)


a =[1,2,3,4]
result = [num * 3 for num in a]
print(result)
