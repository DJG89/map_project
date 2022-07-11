from tkinter import *
from PIL import ImageTk, Image

# dropdown box
japan_provinces = []


def dropbox_command_func(choice):
    #old code
    choice = clicked.get()
    absolute = "japan_maps/"
    path_1 = absolute+choice+"_pol.jpg"
    path_2 = absolute+choice+"_phy.jpg"

    img_1 = Image.open(path_1)
    img_1.show()
    img_2 = Image.open(path_2)
    img_2.show()

def open_japan():
    
    japan_map_path = 'japan_map.jpg'
    japan_img = Image.open(japan_map_path)
    resized = japan_img.resize((378,450))
    global final_resized_img
    final_resized_img=ImageTk.PhotoImage(resized)
    newWindow = Toplevel()
    newWindow.geometry('600x600')
    newWindow.title('Japan Province Viewer')
    japan_label_0 = Label(newWindow, text='Welcome, choose a province')
    japan_label_0.pack()
    japan_label_1 = Label(newWindow, image=final_resized_img, padx=90)
    japan_label_1.pack()

    # variables for dropbox
    #global clicked 
    #clicked = StringVar()
    #clicked.set(vietnam_provinces[0])

    #drop = OptionMenu(newWindow, clicked, *vietnam_provinces, command=dropbox_command_func)
    #drop.pack(pady= 10)
