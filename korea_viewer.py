from tkinter import *
from PIL import ImageTk, Image

import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

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

# The two functions below are for web scraping
def get_entry():
    
    # This function takes value from entry box
    # and passes it to the korea_web_scraper
    # function

    value = entry_box.get()
    return value

def korea_web_scraper():
    city = get_entry()
    page = requests.get(f"https://www.koreaherald.com/search/index.php?kr=&q={city}")

    # Make soup object
    soup = BeautifulSoup(page.content, 'lxml')

    # 1) headers
    headers = []
    header_divs = soup.find_all('div', class_="main_l_t1")
    for div in header_divs:
        headers.append(div.text)

    # 2) captions
    captions = []
    caption_tags = soup.find_all('div', class_="main_l_t3 ellipsis5")
    for tag in caption_tags:
        captions.append(tag.text)

    # 3) links
    final_links = []
    links = soup.select('ul.main_sec_li a')
    string_front = "https://www.koreaherald.com"
    for link in links:
        final_links.append(string_front+link.get('href'))

    # Open file to write your data to
    print(f"getting your news files..")
    now = datetime.now()
    formatted_time = now.strftime("%m/%d/%y, %H:%M")
    with open("korea_news.txt", "a") as file:
        file.write(formatted_time)

    # Write headers, captions, links to file
    # and also close the file
    for h, c, fl in zip(headers, captions, final_links):
        f = open("korea_news.txt", "a")
        print(f"\n{h}\n{c}\n{fl}"+"\n----------", file=f)
    f.close()
    print("you can check your news now...")


# This next function opens window for Korea. It gets 
# called from province_viewer_final.py
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
    drop.pack()

    global entry_box
    entry_box = Entry(newWindow)
    entry_box.pack()

    # this button intiates the web scraper
    scrape_button = Button(newWindow, text='Get News',command=korea_web_scraper)
    scrape_button.pack()

