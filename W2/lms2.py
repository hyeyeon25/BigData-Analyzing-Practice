# random.randrange(5) -> 0 1 2 3 4
# random.randint(1, 5) -> 1 2 3 4 5

import random

n = random.randint(1, 99)
print("오늘의 솟자는 %d\n" %n)
num10 = n//10
num1 = n%10

if num10==0:
    num10=2 # 369 아닌 값
if num1==0:
    num1=2

if num10%3==0 and num1%3==0:
    print("박수 짝!짝!")
elif (num10%3==0 and num1%3!=0) or (num10%3!=0 and num1%3==0):
    print("박수 짝!")
else:
    print("박수 없음")