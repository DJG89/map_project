#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import itertools
import time

def start_scraping(city):
	# do something
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

	print(f"getting your news files...")
	time.sleep(3)
	with open("randomfile.txt", "w") as external_file:
		for h, c, fl in zip(headlines, captions, final_links):
			print(f"{h}{c}\n{fl}"+"\n----------", file=external_file)
		external_file.close()

start_scraping('nanjing')
