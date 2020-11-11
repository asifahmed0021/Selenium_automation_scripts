from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from termcolor import colored
import sys

username=raw_input('Enter your username:')
password=raw_input('Enter your password:')
n=int(input('Enter number of users to unfollow:'))
if(n<=0):
    print(colored('Enter a number greater than 0.','red'))
    sys.exit()

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
    print('Logged in successfully!')
except:
    print(colored('Wrong credentials entered. Try again.','red'))
    sys.exit()

try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
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
    driver.find_element_by_xpath('//div[@class="Fifk5"][5]/span/img').click()
    driver.find_element_by_xpath('//a[@class="-qQT3"][1]').click()
except:
    print(colored('Instagram source code changed.','red'))
    sys.exit()





def delete(n):
    current_following_count=driver.find_element_by_xpath('//li[@class="Y8-fY "][3]/a').text
    print(colored('Current following count:  '+current_following_count,'blue'))
    driver.find_element_by_xpath('//li[@class="Y8-fY "][3]/a').click()
    i=1
    error_count=0
    last_button=driver.find_element_by_xpath('//div[@class="PZuss"]/li[12]/div/div[3]/button')
    while(i<13 and i<=n):
        i1=str(i)
        try:
            path='//div[@class="PZuss"]/li['+i1+']/div/div[3]/button'
            button=driver.find_element_by_xpath(path)
            button.click()
            driver.find_element_by_xpath('//div[@class="mt3GC"]/button[1]').click()
            print('SNo.{} Unfollow attempted on:  '.format(i) +driver.find_element_by_xpath('//div[@class="PZuss"]/li['+i1+']/div/div[2]/div[1]/div/div/span/a').text)
            i+=1
            error_count=0
        except:
            print(colored('Trying to connect again...  Please keep instagram browser open.','blue'))
            error_count+=1
            if(error_count>20):
                print(colored('Program execution stopped due to less number of your following accounts than entered or bad connectivity','red'))
                show_result(i-1)
                sys.exit()
            if i==12:
                break
    i=12
    
    while(i<=n):
        try:
            i1=str(i)
            path='//li[@class="wo9IH"]['+i1+']/div/div[2]/button'
            button=driver.find_element_by_xpath(path)
            button.click()
            driver.find_element_by_xpath('//div[@class="mt3GC"]/button[1]').click()
            print('SNo.{} Unfollow attempted on:  '.format(i) +driver.find_element_by_xpath('//div[@class="PZuss"]/li['+i1+']/div/div[1]/div[2]/div[1]/span/a').text)
            i+=1
            last_button=button
            error_count=0
        except:
            print(colored('Trying to connect again...  Please keep instagram browser open.','blue'))
            error_count+=1
            if(error_count>20):
                print(colored('Program execution stopped due to less number of your following accounts than entered or bad connectivity','red'))
                show_result(i-1)
                sys.exit()
            last_button.send_keys(Keys.DOWN)
    show_result(i-1)


def show_result(n):
    print(colored('Successfully attempted unfollow on {} accounts!'.format(n),'blue'))
    driver.find_element_by_xpath('//div[@class="WaOAr"]/button')
    driver.refresh()
    updated_following_count=driver.find_element_by_xpath('//li[@class="Y8-fY "][3]/a').text
    print(colored('Updated following count:  '+updated_following_count,'green'))
    print(colored('Note:The difference in number of your following accounts may differ from expected, due to instagram\'s maximum unfollowing limit.','yellow'))

delete(n)
