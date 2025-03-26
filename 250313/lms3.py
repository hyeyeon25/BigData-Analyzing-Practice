import random
import time

correctCnt, wrongCnt=0, 0

for i in range(1, 11):
    x = random.randint(1, 99)
    y = random.randint(1, 99)
    print(f'{i}번>> {x}+{y}=')
    startTime = time.time()
    answer = int(input())
    endTime = time.time()

    print("%.1f초 만에 답을 했네요" %(endTime-startTime))
    if answer == x+y:
        print("정답입니다.")
        correctCnt += 1
    else:
        print("오답입니다.")
        wrongCnt += 1