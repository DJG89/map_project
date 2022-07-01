# import statements
from bs4 import BeautifulSoup
from datetime import datetime
from secrets import choice
from tkinter import *
from PIL import ImageTk, Image
from japan_viewer import *
from korea_viewer import *
from vietnam_viewer import *
import requests
import itertools
import time
import sys


# the first thing you always do
root = Tk()
root.title("Province Viewer")

# Label widget 1
label_1 = Label(root, text="Welcome, choose a province", padx=90)
label_1.grid(row=0, column=0)

# Menu for the top of the window
menu_bar = Menu(root)

# When you make a menu, you also have to configure it
root.config(menu=menu_bar)



# menu bar items
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Switch to Korea Map',command=open_korea)
file_menu.add_command(label='Switch to Japan Map',command=open_japan)
file_menu.add_command(label='Switch to Vietnam Map',command=open_vietnam)
file_menu.add_separator()
file_menu.add_command(label='Quit',command=root.quit)




# Label widget 2
#label_2 = Label(root, text="Choices go here")
#label_2.grid(row=2, column=0)



china_map_path = 'china_map.jpg'
my_img = ImageTk.PhotoImage(Image.open(china_map_path))
image_label = Label(image=my_img)
image_label.grid(row=1, column=0)


# Physical Map widget
# physical_frame = Frame(root, bg="blue",pady=50)
# physical_frame.grid(rowspan=3, column=1)

# dropdown box
provinces = [
    "Anhui", "Beijing", "Chongqing",
    "Fujian", "Gansu", "Guangdong",
    "Guangxi", 
    "Guizhou", "Hainan", "Hebei",
    "Heilongjiang", "Henan",
    "Hong Kong", "Hubei",
    "Hunan", "Inner Mongolia", "Jiangsu",
    "Jiangxi", "Jilin", "Liaoning",
    "Macau", "Ningxia", "Qinghai",
    "Shaanxi", "Shandong", "Shanghai",
    "Shanxi", "Sichuan", "Tianjin",
    "Tibet", "Xinjiang",
    "Yunnan", "Zhejiang"
]

clicked = StringVar()
clicked.set(provinces[0])

def get_entry():
    value = my_box.get()
    return value

def start_scraping():
    # do something
    city = get_entry()
    
    html_text = requests.get(f'http://was.cipg.org.cn/was5/web/search?searchword={city}&channelid=209889').text
    
    
    soup = BeautifulSoup(html_text, 'lxml')
    rows = soup.find_all('tr')

    
    
    first_link = soup.find('a')
    links = []
    headlines = []
    captions = []
    for row in rows[3:-2:2]:
        headlines.append(row.text)

    for row in rows[4:-2:2]:
        captions.append(row.text)

    for link in soup.find_all('a'):
        links.append(link.get('href'))

    final_links = []

    for link in links[4:-12]:
        final_links.append(link)

    print(f"getting your news files..")
    now = datetime.now()
    formatted_time = now.strftime("%m/%d/%y, %H:%M")
    with open("scraped_news.txt", "a") as file:
        file.write(formatted_time)

    for h, c, fl in zip(headlines, captions, final_links):
        f = open("scraped_news.txt", "a")
        print(f"{h}{c}\n{fl}"+"\n----------", file=f)
    f.close()
    print("you can check your news now...")


def my_func_1(choice):
    choice = clicked.get()
    print(choice)

def my_func_2(choice):
    # show maps
    choice = clicked.get()
    absolute = "maps/"
    path_1 = absolute+choice+"_pol.jpg"
    path_2 = absolute+choice+"_phy.jpg"
    img_1 = Image.open(path_1)
    img_1.show()
    img_2 = Image.open(path_2)
    img_2.show()

drop = OptionMenu(root, clicked, *provinces, command=my_func_2)
drop.grid(row=2)


# web scrape entry box
my_box = Entry(root)
my_box.insert(0, "Type province for news info")
my_box.grid(row=3, column=0)

# web scraper button
firstbtn = Button(root, text='Get News',command=start_scraping)
firstbtn.grid(row=4, column=0)

root.mainloop()


'''
img_1 = Image.open(path)
img_1.show()
'''
