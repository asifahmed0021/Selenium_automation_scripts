from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from termcolor import colored
import sys

username=raw_input('Enter your username:')
password=raw_input('Enter your password:')
target=raw_input('Enter username to whose followers you want to send request:')
n=input('Enter number of users to send request to:')


try:
    driver=webdriver.Chrome('../chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.instagram.com')
    print('Browser opened successfully!')
except:
    print(colored('Check your internet connection and try again.','red'))
    sys.exit()

try:
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    print(colored('Logged in successfully!','green'))
except:
    print(colored('Wrong credentials entered. Try again.','red'))
    sys.exit()


try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
except:
    print('Source code changed a little but no worries here..')
try:
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
except:
    print('Source code changed a little but no worries here..')


try:
    driver.find_element_by_xpath("//input[@type='text']").send_keys(target)
    driver.find_element_by_xpath("//a[@class='yCE8d  ']").click()
    driver.find_element_by_xpath("//li[@class='Y8-fY '][2]/a").click()
except:
    print(colored('Either the account does not exist or it is private','red'))
    sys.exit()


i=1
last_button=driver.find_element_by_xpath("//div[@class='PZuss']/li[10]/div/div[3]/button")
driver.implicitly_wait(3)
sent=0
error_count=0
while(i<13 and sent<=n):
    i1=str(i)
    try:
        userid=driver.find_element_by_xpath("//div[@class='PZuss']/li["+i1+"]/div/div[2]/div/div/div/span/a").text
        path="//div[@class='PZuss']/li["+i1+"]/div/div[3]/button"
        button=driver.find_element_by_xpath(path)
        if not(button.text=='Following' or button.text=='Requested'):
            button.click()
            print('SNo.:{}  Request sent to         {}'.format(i,userid))
            sent+=1
        elif button.text=='Following':
            print('SNo.:{}  Already following       {}'.format(i,userid))
        else:
            print('Sno.:{}  Already requested to    {}').format(i,userid)
        i+=1

    except:
        print(colored('Trying to connect again...  Please keep instagram browser open.','blue'))
        error_count+=1
        if(error_count>=20):
            print(colored('Program execution stopped due to low number of followers of target account or bad connectivity','red'))
            print(colored('Successfully sent follow request to {} accounts'.format(sent),'green'))
            sys.exit()
        last_button.send_keys(Keys.DOWN)



while(sent<=n):
    i1=str(i)
    try:
        userid=driver.find_element_by_xpath("//div[@class='PZuss']/li["+i1+"]/div/div[1]/div[2]/div[1]/span/a").text
        path="//div[@class='PZuss']/li["+i1+"]/div/div[2]/button"
        button=driver.find_element_by_xpath(path)
        if not(button.text=='Following' or button.text=='Requested'):
            button.click()
            print('SNo.:{}  Request sent to         {}'.format(i,userid))
            sent+=1
        elif button.text=='Following':
            print('SNo.:{}  Already following       {}'.format(i,userid))
        else:
            print('Sno.:{}  Already requested to    {}').format(i,userid)
        i+=1
        last_button=button
    except:
        print(colored('Trying to connect again...  Please keep instagram browser open.','blue'))
        error_count+=1
        if(error_count>=20):
            print(colored('Program execution stopped due to low number of followers of target account or bad connectivity','red'))
            print(colored('Successfully sent follow request to {} accounts'.format(sent),'green'))
            sys.exit()
        last_button.send_keys(Keys.DOWN)

print(colored('Successfully sent follow request to {} accounts'.format(sent-1),'green'))
