import random

number = []

for i in range(1,11):
    num = random.randint(1,46)
    number.append(num)

print("생성된 값", number)
find = False
userNo = int(input("찾을 키 값 입력>>"))
for i in number:
    if i==userNo:
        print("리스트에서 찾았습니다 !!")
        #exit(1)
        find = True
        break
if find == False:
    print("리스트에 없는 값입니다.")