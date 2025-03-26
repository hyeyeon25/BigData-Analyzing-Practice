'''for문 활용
3~100까지의 숫자 중 소수를 모두 출력, 소수의 개수 출력'''

primeCnt = 0
for n in range(3, 101):
    sosu = True
    for i in range(2, n):
        if n % i != 0:
            continue
        else:
            sosu = False
            break
    if sosu==True:
        primeCnt += 1
        print("%5d" % n, end =" ")

print("\n3~100까지 소수의 개수 = %d" %primeCnt)
