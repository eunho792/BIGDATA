money = True

if money:

    print("택시를 타고 가라")

else:

    print("걸어 가라")


money = 2000

card = True

if money >= 3000 or card:
    print("택시를 타고 가라")

else:
    print("걸어가라")


pocket = ['paper','cellphone','money']
if 'money' in pocket:
    print("택시타고 가라")
else:
    print("걸어가라")

score = 70
message = "success" if score >= 60 else "faulure"
