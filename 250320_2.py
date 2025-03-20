'''리스트를 이용한 친구 관리 프로그램'''
def Menu():
    print("-"*20)
    print("[1] 친구 추가")
    print("[2] 친구 변경")
    print("[3] 친구 삭제")
    print("[4] 친구 명단 보기")
    print("[5] 종료")
    print("-"*20)

friend = []
choice = 0

while choice != 5:
    Menu()      # 함수 호출
    choice = int(input("메뉴 선택>> "))

    if choice == 1:
        name = input("등록할 친구의 이름 입력>> ")
        friend.append(name)
        print("등록 완료!")

    elif choice == 2:
        OldName = input("변경할 친구의 이름 입력>> ")
        if OldName in friend:               # 변경할 이름이 리스트에 있는 경우
            no = friend.index(OldName)      #방번호 찾기
            NewName = input("새로운 이름 입력>> ")
            friend[no] = NewName
            print("이름 변경 완료!")
        else: print(OldName + "이란 친구는 없습니다.")

    elif choice == 3:
        DelName = input("삭제할 친구의 이름 입력>> ")
        if DelName in friend:               # 변경할 이름이 리스트에 있는 경우
            friend.remove(DelName)
            '''no = friend.index(DelName)
            del(friend[no])'''
            print("삭제되었습니다.")

        else:
            print(DelName + "이란 친구는 없습니다.")

    elif choice == 4:
        if len(friend) == 0:                # 리스트가 빈 경우
            print("등록된 친구가 없습니다.")
            continue
        else:
            print(friend)
