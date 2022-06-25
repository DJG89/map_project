## China Japan Korea Vietnam Map Project

# Project Description
The point of this project is to create a Python GUI using Tkinter that can display geographical as well as statistical (is that a word?) information about every province of China, Japan, Korea, and Vietnam. The idea is to help people who want be a little bit more familiar with these countries. Hopefully, later we can implement a SQL database as a part of this project.

# How to Run the Project
* Make sure you have at least Python 3
* Run 'province_viewer_final.py'

# How to Use the Project
* Once you are able to open the GUI:
    * You will see a map of China
    * The dropdown menu let's you choose a province in China
    * After you select a province, a physical map and a political map of that province will come up.
    * The entry box that say's "Type province for news info" - That is the web scraper functionality. 
        *You just need to input a city or province in China. Make sure it is
    * In the terminal, if you get an error, it probably means you just can't access the Beijing Review website from your country.I've only used this app within China. Not sure if it works abroad. sry lol
    * If the scraper works correctly, you should see "getting your news files.." in the terminal. 
    * The news gets stored in a file called 'scraped_files.txt'..the file should have the date, headlines, and links to those headlines.