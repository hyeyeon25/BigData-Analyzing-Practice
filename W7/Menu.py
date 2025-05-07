from tkinter import *
from tkinter.filedialog import *   # 열기 대화상자 창

#[불러오기] 메뉴를 선택했을 때 동작 함수
def openFunc():
    askopenfilename()  #"열기" 대화상자
    filename = askopenfilename(parent = window)
    #"쓰기" 대화상자 : asksaveasfile()

    photo = PhotoImage(file = filename)
    # pLabel["image"] = photo   #밑에줄하고 외우기
    pLabel.config(image = photo)
    pLabel.image = photo
    wLabel["text"] = filename
#[프로그램 종료] 메뉴를 선택했을 때 동작 함수
def exitFunc():
    window.quit() #이거 두줄 외우기
    window.destroy()

window = Tk()
window.geometry("500x500")
window.title("메뉴만들기")

#gif 이미지를 담을 객체 생성
photo = PhotoImage
#이미지가 출력될 라벨 생성하고 부착
pLabel = Label(window, text = "여기에 이미지가 출력됩니다.")
pLabel.pack(anchor = "center")  #중앙 정렬

#[File] 메인메뉴 생성
mainMenu = Menu(window) #윈도우창의 메뉴영역을 생성
window.config(menu = mainMenu) # window["menu"] = mainMenu 코드와 동일
fileMenu = Menu(mainMenu)  # 메뉴영역에 들어갈 fileMenu 선언
mainMenu.add_cascade(label = "File", menu = fileMenu)

# 이거 시험에 낸다는듯
#서브메뉴 생성 - [불러오기] 와 [프로그램 종료]
fileMenu.add_command(label = "불러오기", command = openFunc)
fileMenu.add_command(label = "프로그램 종료", command = exitFunc)

# 불러온 파일의 정보 출력할 라벨 생성
wLabel = Label(window, text="여기에 파일의 정보가 출력됩니다.")
wLabel.pack()
window.mainloop()