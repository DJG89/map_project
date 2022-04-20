# import statements
from tkinter import *
from PIL import ImageTk, Image


# the first thing you always do
root = Tk()
root.title("Korean Province Viewer")


# Label widget 1
label_1 = Label(root, text="Welcome, choose a province", padx=90)
label_1.grid(row=0, column=0)

korea_map_path = '/Users/daringallowjr/Desktop/map_project/korea_map.jpg'
my_img = ImageTk.PhotoImage(Image.open(korea_map_path))
image_label = Label(image=my_img)
image_label.grid(row=1, column=0)


# dropdown box
provinces = [
    "Seoul", "Incheon", "Busan",
    "Chungcheong-North", "Chungcheong-South",
    "Daegu", "Daejeon", 
    "Gangwon", "Gwangju", "Gyeonggi",
    "Gyeongsang-North", "Gyeongsang-South",
    "Jeju", "Jeolla-North", "Jeolla-South", 
    "Sejong"
]

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


root.mainloop()