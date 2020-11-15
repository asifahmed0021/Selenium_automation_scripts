from selenium import webdriver
import time
from termcolor import colored
import sys
import pyautogui as gui

print(colored('Note:Please make sure you have whatsapp desktop installed and connected with your phone with the QR code scanned.','yellow'))

#input
number=input('Enter contact number to spam with country code:')
message=input('Enter spam message:')
spam_length=int(input('Enter number of messages you want to send:'))

driver=webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.implicitly_wait(100)

driver.get('https://wa.me/{}?text='.format(number))
time.sleep(20)
gui.click(gui.locateOnScreen('alert.png'))
time.sleep(5)

for i in range(spam_length):
    print('{} out of {} sent'.format(i+1,spam_length))
    gui.write(message)
    gui.press('enter')

print(colored('Total {} spam messages sent to {}'.format(spam_length,number),'green'))

