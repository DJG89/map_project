import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

city = input("enter a city in South Korea: ")
page = requests.get(f"https://www.koreaherald.com/search/index.php?kr=&q={city}")

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

## Write everything to file
print(f"getting your news files..")
now = datetime.now()
formatted_time = now.strftime("%m/%d/%y, %H:%M")
with open("korea_news.txt", "a") as file:
	file.write(formatted_time)

for h, c, fl in zip(headers, captions, final_links):
        f = open("korea_news.txt", "a")
        print(f"\n{h}\n{c}\n{fl}"+"\n----------", file=f)
f.close()
print("you can check your news now...")

