# 리스트에 6개의 이미지를 저장, [이전] [다음] 버튼 생성을 하여
# 버튼을 눌렀을 때 이미지 라벨레 리스트의 이미지들이 출력
from tkinter import *

#인덱스       0         1         2         3         4         5
fname = ["d1.gif", "d2.gif", "d3.gif", "d4.gif", "d5.gif", "d6.gif"]
photoList = [None] * 6
num = 0    # 기본 보여질 이미지의 인덱스번호 0으로 초기화

# [이전] 버튼을 눌렀을 때 동작 함수
def PrevFunc():    # 이 함수 출제
    global num
    num -= 1

    if num < 0:
        num = 5
    photo = PhotoImage(file='../media/' + fname[num])
    pLabel["image"] = photo
    pLabel.image = photo

# [다음] 버튼을 눌렀을 때 동작 함수
def NextFunc():
    global num
    num += 1    # 인덱스 번호 1씩 증가

    if num > 5:
        num = 0    # 끝 인덱스까지 갔으면 0으로 돌아가기
    photo = PhotoImage(file='media/'+fname[num])    # 가져올 파일명: img/d1.gif
    pLabel["image"] = photo
    pLabel. image = photo    # 라벨에 이미지 출력

window = Tk()
window.geometry("400x400")
window.title("이미지 앨범 만들기")

#버튼 2개 생성하여 부착
prevBtn = Button(window, text="이전",width=15,command=PrevFunc)
nextBtn = Button(window, text="다음",width=15,command=NextFunc)
prevBtn.place(x=150,y=30)
nextBtn.place(x=290,y=30)

# 라벨 생성 부착
photo = PhotoImage(file='media/'+fname[0])
pLabel = Label(window,image=photo)
pLabel.place(x=150,y=80)

window.mainloop()