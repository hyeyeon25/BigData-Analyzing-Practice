from tkinter import *
window = Tk()

def Year():
    if val.get()==1:
        l1["text"]="1학년 입니다."
    elif val.get()==2:
        l1["text"]="2학년 입니다."
    elif val.get()==3:
        l1.configure(text="3학년 입니다.")
    else:
        l1.configure(text="4학년 입니다.")
def Func():
    if chk.get()==1:
        print("당신의 취미는 수영입니다.")
    else:
        print("취미가 없네요")


val = IntVar()
rb1 = Radiobutton(window, text="1학년", variable=val, value=1, command=Year)
rb2 = Radiobutton(window, text="2학년", variable=val, value=2, command=Year)
rb3 = Radiobutton(window, text="3학년", variable=val, value=3, command=Year)
rb4 = Radiobutton(window, text="4학년", variable=val, value=4, command=Year)

l1 = Label(window, text="학년 정보 출력", fg="blue")

chk = IntVar()
ch1 = Checkbutton(window, text="수영", variable=chk, command=Func)
ch1.pack()

rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()
l1.pack()

window.mainloop()