from tkinter import *
from PIL import ImageTk, Image

# dropdown box
korea_provinces = [
    "Seoul",
    "North Chungcheong", "South Chungcheong",
    "Gangwon", "Gyeonggi", 
    "North Gyeongsang", "South Gyeongsang",
    "North Jeolla", "South Jeolla", 
    "Jeju"
]


def dropbox_command_func(choice):
    #old code
    choice = clicked.get()
    absolute = "korea_maps/"
    path_1 = absolute+choice+"_pol.jpg"
    path_2 = absolute+choice+"_phy.jpg"

    img_1 = Image.open(path_1)
    img_1.show()
    img_2 = Image.open(path_2)
    img_2.show()

def open_korea():
    global korea_img
    korea_map_path = 'korea_map.jpg'
    korea_img = ImageTk.PhotoImage(Image.open(korea_map_path))
    newWindow = Toplevel()
    newWindow.title('Korea Province Viewer')
    korea_label_0 = Label(newWindow, text='Welcome, choose a province')
    korea_label_0.pack()
    korea_label_1 = Label(newWindow, image=korea_img, padx=90)
    korea_label_1.pack()

    # variables for dropbox
    global clicked 
    clicked = StringVar()
    clicked.set(korea_provinces[0])

    drop = OptionMenu(newWindow, clicked, *korea_provinces, command=dropbox_command_func)
    drop.pack(pady= 10)

'''
clicked = StringVar()
clicked.set(provinces[0])

def my_func_2(choice):
    # show maps
    choice = clicked.get()
    absolute = "/Users/daringallowjr/Desktop/map_project/korea_maps/"
    path_1 = absolute+choice+"_pol.jpg"
    path_2 = absolute+choice+"_phy.jpg"
    img_1 = Image.open(path_1)
    img_1.show()
    img_2 = Image.open(path_2)
    img_2.show()

drop = OptionMenu(root, clicked, *provinces, command=my_func_2)
drop.grid(row=2)
'''