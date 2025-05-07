from tkinter import *

window = Tk()


counter = 0 #전역변수 counter를 선언함

def clicked():
    global counter #전역변수 counter를 사용
    counter += 1
    label['text'] = '버튼 클릭 횟수: ' + str(counter) #레이블 객체가 가진 ‘text’ 속성은 딕셔너리처럼 찾음

label = Label(window, text="아직 눌려지지 않음")
label.pack()
button = (Button(window, text="증가", command=clicked))
button.pack()

window.mainloop()
