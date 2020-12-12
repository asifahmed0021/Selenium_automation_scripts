from selenium import webdriver
import time
from termcolor import colored
import sys
from selenium.webdriver.support.ui import WebDriverWait 

#ldap credentials input
username=input('Enter your LDAP userid: ')
password=input('Enter your LDAP password: ')

#opening browser
driver=webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.implicitly_wait(50)

#entering login details
try:
    driver.get('http://172.16.100.161:8080/Aryabhatta')
    username_input=driver.find_element_by_xpath('//form[@name="AryabhattaForm"]/div/input[1]')
    username_input.clear()
    username_input.send_keys(username)

    pass_input=driver.find_element_by_xpath('//form[@name="AryabhattaForm"]/div/input[2]')
    pass_input.clear()
    pass_input.send_keys(password)

    button=driver.find_element_by_xpath('//form[@name="AryabhattaForm"]/input')
    button.click()
except:
    print(colored('Not able to connect. Please check your internet connection and proxy settings.','red'))
    sys.exit()

driver.implicitly_wait(3)

#authenticating
try:
    driver.find_element_by_xpath('//div[@class="error"]')
    print(colored('LDAP authentication failed. Please provide valid LDAP credentials.','red'))
    sys.exit()
except:
    print('Logged in successfully!')
    print('...............................................')
driver.implicitly_wait(30)

#fetching data
try:
    name=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/div/div[1]/div/div/h3/a').text
    roll_no=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/div/div[1]/div/div/p[1]').text
    degree=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/div/div[1]/div/div/p[2]').text
    discipline=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/div/div[1]/div/div/p[3]').text
    supervisor=driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/div/div[2]/div/div/h3/a').text

    num_courses=int(driver.find_element_by_xpath('//div[@id="page-wrapper"]/div/div[1]/div[1]/div/div/a/h5').text)
    creds=driver.find_element_by_xpath('//div[@id="page-wrapper"]/div/div[1]/div[2]/div/div/h5').text
    cg=driver.find_element_by_xpath('//div[@id="page-wrapper"]/div/div[1]/div[3]/div/div/h5').text
except:
    print(colored('Bad network connection. Please try again.','red'))
    sys.exit()


print(colored('Students Name: {}'.format(name),'green'))
print(colored('Roll number: {}'.format(roll_no),'green'))
print(colored(degree,'green'))
print(colored(discipline,'green'))

print('...............................................')

print(colored('Supervisor Name: {}'.format(supervisor),'yellow'))
print(colored('Credits completed: {}'.format(creds),'yellow'))

print('...............................................')


try:
    driver.find_element_by_xpath('//div[@class="left-side-inner"]/ul/li[2]/a').click()
    driver.find_element_by_xpath('//div[@class="left-side-inner"]/ul/li[2]/ul/li[3]/a').click()
    table=driver.find_element_by_xpath('//div[@class="bs-example"]/table/tbody/tr/td/table/tbody')
except:
    print(colored('Bad network connection. Please try again.','red'))
    sys.exit()


code_list=[]
course_list=[]
credit_list=[]
slot_list=[]

#fetching course data
for i in range(2,num_courses+2):
    code_list.append(table.find_element_by_xpath('tr[{}]/td[2]'.format(i)).text)
    course_list.append(table.find_element_by_xpath('tr[{}]/td[3]'.format(i)).text)
    credit_list.append(table.find_element_by_xpath('tr[{}]/td[4]'.format(i)).text)
    slot_list.append(table.find_element_by_xpath('tr[{}]/td[6]'.format(i)).text)

def convert(s):
    for i in range(16-len(s)):
        s+=" "
    return s

print(colored('{}{}{}{}'.format(convert('Course code'),convert('Slot number'),convert('Credits'),convert('Course name')),'blue'))

for i in range(len(code_list)):
    print(colored('{}{}{}{}'.format(convert(code_list[i]),convert(slot_list[i]),convert(credit_list[i]),convert(course_list[i])),'cyan'))
