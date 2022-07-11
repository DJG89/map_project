from tkinter import *
from PIL import ImageTk, Image

# dropdown box
korea_provinces = [
    "Seoul", "Incheon",
    "North_Chungcheong", "South_Chungcheong",
    "Gangwon", "Gyeonggi", "Ulsan","Busan",
    "North_Gyeongsang", "South_Gyeongsang","Daegu",
    "North_Jeolla", "South_Jeolla","Daejeon",
    "Sejong_City", "Jeju"
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
    
    korea_map_path = 'korea_map_2.jpg'
    korea_img = Image.open(korea_map_path)
    resized = korea_img.resize((400,500))
    global final_resized_img
    final_resized_img=ImageTk.PhotoImage(resized)
    newWindow = Toplevel()
    newWindow.geometry('600x600')

    newWindow.title('Korea Province Viewer')
    korea_label_0 = Label(newWindow, text='Welcome, choose a province')
    korea_label_0.pack()
    korea_label_1 = Label(newWindow, image=final_resized_img, padx=90)
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