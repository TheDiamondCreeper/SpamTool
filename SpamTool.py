from pyautogui import press
from pyautogui import write
from tkinter import *
from time import sleep as s

root = Tk()
root.geometry('325x75')
root.title('Spam Tool')
root.resizable(0, 0)

spam_ico = PhotoImage(file = r'C:\Users\youss\Desktop\py\Spam Tool\\TextPNG.png')
root.iconphoto(False, spam_ico)

def spamming():
    number_of_spamming = int(Num.get()) + 1
    Text_to_send = str(text.get())
    s(5)
    for i in range(1, number_of_spamming):
        write(Text_to_send)
        press('enter')

credits = Label(root, text='SpamTool by Youssef Elebiary', fg='azure4').place(x=17.5, y=55)

text = Entry(root)
text.place(x=50, y=5, width=140)

text_lbl = Label(root, text='Text', font=('bold')).place(x=10, y=1)

Num = Entry(root)
Num.place(x=65, y=35, width=125)

num_lbl = Label(root, text='Times', font=('bold')).place(x=10, y=31)

Btn = Button(root, text="Spam", width=12, height=3, bg='red', font=('bold'), command=spamming).place(x=200, y=4)

root.mainloop()