from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import sys
from termcolor import colored
#inputs
username=str (raw_input('Enter your instagram username:'))
password=str (raw_input('Enter your password:'))


driver=webdriver.Chrome('../chromedriver')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.instagram.com')
print('Browser opened successfully!')

try:
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
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
    driver.find_element_by_xpath('//div[@class="Fifk5"][4]/a').click()
    driver.find_element_by_xpath('//div[@class="f7Bj3"]/div/div/div/div[1]').click()
except:
    print(colored('Instagram source code changed.','red'))
    sys.exit()

i=1
while(True):
    try:
        i1=str(i)
        path='//div[@class="_01UL2"]/div/div/div[1]/div/div['+i1+']/div[3]/div/div[1]/button'
        driver.find_element_by_xpath(path).click()
        print('Request accepted of:   '+driver.find_element_by_xpath('//div[@class="f7Bj3"]/div/div[1]/div/div['+i1+']/div[2]/div/a').text)
        i+=1
    except:
        if i==1:
            print(colored('All requests already accepted','green'))
            break
        print(colored('All {} requests accepted successfully'.format(i-1),'green'))
        break