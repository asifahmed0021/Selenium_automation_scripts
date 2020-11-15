from selenium import webdriver
import time
import sys
from termcolor import colored
import pyautogui as gui
import pandas as pd
import csv

print(colored('Note:Please make sure you have whatsapp desktop installed and connected with your phone with the QR code scanned.','yellow'))

#opening chrome browser
driver=webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.implicitly_wait(20)

#name,contact and message lists
name_list=[]
contact_list=[]
message_list=[]

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name_list.append(row[0])
        contact_list.append(row[1])
        message_list.append(row[2])

length=len(name_list)
name_list=name_list[1:length]
contact_list=contact_list[1:length]
message_list=message_list[1:length]
length-=1

#opening whatsapp for the first time to initialise
driver.get('https://wa.me/+919685422752?text=')
time.sleep(20)

gui.click(gui.locateOnScreen('alert.png'))
time.sleep(5)
gui.click(gui.locateOnScreen('minimize.png'))

#sending messages to all valid contacts
for i in range(0,length):
    try:
        url='https://wa.me/{}?text={}from{}'.format(contact_list[i],message_list[i],name_list[i])
        driver.get(url)
        time.sleep(2)
        gui.click(gui.locateOnScreen('ok.png'))
        time.sleep(2)
        gui.click(gui.locateOnScreen('alert.png'))
        time.sleep(2)
        gui.press('enter')
        time.sleep(2)
        gui.click(gui.locateOnScreen('minimize.png'))
    except:
        print(colored('Some erroe occured','red'))
        sys.exit()


print(colored('Successfully sent messages to all the valid contacts!','green'))
