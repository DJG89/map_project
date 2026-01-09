from tkinter import *

def start_the_box():
    newWindow = Toplevel()
    newWindow.geometry('601x600')
    newWindow.title('GPT Chat Window')

    Label(newWindow, text='GPT Chat Box').pack(pady=5)

    frame = Frame(newWindow)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text_box = Text(
        frame,
        wrap=WORD,
        yscrollcommand=scrollbar.set
    )
    text_box.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=text_box.yview)