def menu():
    print("1. 섭씨 -> 화씨")
    print("2. 화씨 -> 섭씨")
    print("3. 종료")
    user = int(input("메뉴를 선택하세요>>>"))
    return user

def inputC():
    c = float(input("섭씨온도 입력 : "))
    return c

def ctof(temp):
    ftemp = (temp)*9.0/5 + 32
    return ftemp

def inputF():
    f = float(input("화씨온도 입력 : "))
    return f

def ftoc(temp):
    ctemp = (temp-32)*5/9
    return ctemp

def main():
    while True:
        sel = menu()
        if sel == 1:
            temp = inputC()
            tt = ctof(temp)
            print("섭씨 %.1f도 -> 화씨 %.1f도" %(temp,tt))
        elif sel == 2:
            temp = inputF() # inputF() 구현
            tt = ftoc(temp) #ftoc() 구현
            print("화씨 %.1f도 -> 섭씨 %.1f도" %(temp,tt))
        elif sel == 3:
            print("온도 변환 프로그램을 종료합니다.")
            break
        else:
            print("1~3 사이의 메뉴를 선택해야 합니다.")
            continue

main()