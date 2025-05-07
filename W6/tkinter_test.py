from tkinter import *
import random

# 정답세팅
answer = random.randint(1, 100)     # answer = 1부터 100 사이의 수
cnt = 0

def guess():
    global cnt
    user = int(guessField.get())        # 엔트리에 입력된 값 가져오기

    cnt += 1        # 도전 횟수
    if user == answer:
        msg = "정답! %d번째 도전만에 성공" % cnt
    elif user < answer:
        msg = "Up. " + str(user) + "보다 큰 수입니다."
    else:
        msg = "Down. " + str(user) + "보다 작은 수입니다."

    # resultLabel["text"] = msg
    resultLabel.config(text=msg)
    guessField.delete(0, 5)

def reset(): # 정답을 다시 설정한다.
    global answer
    answer = random.randint(1,100)
    resultLabel["text"] = "다시 한번 하세요!"

window = Tk()
window.config(bg="white")
window.title("숫자를 맞혀 보세요!")

window.geometry("500x80")
titleLabel = Label(window, text="숫자 게임에 오신 것을 환영합니다!",bg="white")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side="left")
tryButton = Button(window, text="시도", fg="green", bg="white", command=guess)
tryButton.pack(side="left")

resetButton = Button(window, text="초기화", fg="red", bg="white", command=reset)
resetButton.pack(side="left")
resultLabel = Label(window, text="1부터 100사이의 숫자를 입력하시오.", bg="white")
resultLabel.pack(side="left")

window.mainloop()
