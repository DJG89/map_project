from tkinter import *
from PIL import ImageTk, Image

# dropdown box
vietnam_provinces = ['Hanoi', 'Binh_Duong']


def dropbox_command_func(choice):
    #old code
    choice = clicked.get()
    absolute = "vietnam_maps/"
    path_1 = absolute+choice+"_pol.jpg"
    path_2 = absolute+choice+"_phy.jpg"

    img_1 = Image.open(path_1)
    img_1.show()
    img_2 = Image.open(path_2)
    img_2.show()

def open_vietnam():
    
    vietnam_map_path = 'vietnam_map.jpg'
    vietnam_img = Image.open(vietnam_map_path)
    resized = vietnam_img.resize((400,500))
    global final_resized_img
    final_resized_img=ImageTk.PhotoImage(resized)
    newWindow = Toplevel()
    newWindow.geometry('650x650')
    newWindow.title('Vietnam Province Viewer')
    vietnam_label_0 = Label(newWindow, text='Welcome, choose a province')
    vietnam_label_0.pack()
    vietnam_label_1 = Label(newWindow, image=final_resized_img, padx=90)
    vietnam_label_1.pack()

    # variables for dropbox
    global clicked 
    clicked = StringVar()
    clicked.set(vietnam_provinces[0])

    drop = OptionMenu(newWindow, clicked, *vietnam_provinces, command=dropbox_command_func)
    drop.pack(pady= 10)
