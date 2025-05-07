from tkinter import *
import random

# 윈도우 생성
window = Tk()
window.title("가위바위보 게임")

# 이미지 불러오기
s_img = PhotoImage(file="../media/RSP_Img/scissors.png")
r_img = PhotoImage(file="../media/RSP_Img/rock.png")
p_img = PhotoImage(file="../media/RSP_Img/paper.png")

# 라벨 - 안내 메시지
lbl = Label(window, text="클릭하세요", font=("Mistral", 20, "bold"))
lbl.pack()

# 컴퓨터 이미지 표시용 라벨
com_img = Label(window, image=None)
com_img.pack()

# 결과 메시지 라벨
result_lbl = Label(window, text="", font=("Mistral", 16))
result_lbl.pack()

# 가위 버튼 클릭 시
def pass_s():
    decide("가위")

# 바위 버튼 클릭 시
def pass_r():
    decide("바위")

# 보 버튼 클릭 시
def pass_p():
    decide("보")

# 승부 결정 함수
def decide(human):
    com = random.choice(["가위", "바위", "보"])

    # 이미지 업데이트
    if com == "가위":
        com_img.config(image=s_img)
    elif com == "바위":
        com_img.config(image=r_img)
    elif com == "보":
        com_img.config(image=p_img)

    # 승패 결정
    if human == com:
        result = "무승부!"
    elif (com == "가위" and human == "보") or \
            (com == "바위" and human == "가위") or \
            (com == "보" and human == "바위"):
        result = "졌습니다!"
    else:
        result = "이겼습니다!"

    # 결과 출력
    result_lbl.config(text=f"당신: {human}, 컴퓨터: {com} → {result}")

# 버튼 생성
frame = Frame(window)
frame.pack()

btn_s = Button(frame, text="가위", width=10, command=pass_s)
btn_r = Button(frame, text="바위", width=10, command=pass_r)
btn_p = Button(frame, text="보", width=10, command=pass_p)

btn_s.pack(side=LEFT, padx=5, pady=10)
btn_r.pack(side=LEFT, padx=5, pady=10)
btn_p.pack(side=LEFT, padx=5, pady=10)

# GUI 실행
window.mainloop()
