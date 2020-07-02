a=1
sum=0
while(a<=1000):
    if(a%3==0):
        sum+=a
        a+=1
    else:
        a+=1
        continue
print(sum)

b= "*"
c= 1
while(c<6):
    print(b*c)
    c+=1;

sum=0
for a in range(1,101):
    print(a,end=" ")
print("")


A =[70,60,55,75,95,90,80,80,85,100]
for i in A:
    sum = sum+i
avg =sum/len(A)
print("평균",avg)

