from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
import csv



file = open('c:/Users/tyler/OneDrive/Documents/Python_Scripts/Job_Hunt.csv', 'w')
writer = csv.writer(file)
# writerow() method to the write to the file object
writer.writerow(['Job Title', 'Company', 'Location', 'URL'])

#retrieve login info from file
with open("c:/Users/tyler/OneDrive/Documents/Python_Scripts/Sensitive.txt" ,"r") as login:
    user = login.readline()
    passwd = login.readline()


driver = webdriver.Chrome('c:/Users/tyler/OneDrive/Documents/Python_Scripts/chromedriver')
driver.get('https://www.linkedin.com/login')
t.sleep(0.5)

#fill in username
username = driver.find_element_by_id("username")
username.send_keys(user)
t.sleep(1.5)

#fill in password
password = driver.find_element_by_id("password")
password.send_keys(passwd)
t.sleep(1.5)

#sign in - delays added for slow loading speed errors
sign_in = driver.find_element_by_css_selector('#app__container > main > div:nth-child(2) > form > div.login__form_action_container > button')
sign_in.click()
t.sleep(5)

#click jobs section
Jobs = driver.find_element_by_link_text("Jobs")
Jobs.click()
t.sleep(1.5)


Searchbar = driver.find_elements_by_xpath("//div/div/div/div/div/input")
Searchbar[0].send_keys("Student")
t.sleep(1.0)
# Searchbar[2].send_keys("Israel")
# t.sleep(0.5)

Searchbar[2].send_keys(Keys.ENTER)
t.sleep(3.0)

listings = driver.find_elements_by_class_name("job-card-list__title")
page = driver.find_elements_by_xpath("//li/button/span")
pg=1
# links = driver.find_elements_by_xpath("li//div/div/div/div/div/a")
for i in range(len(page)):
    if pg>len(page):
        break
    # print (i.text)
    listings = driver.find_elements_by_class_name("job-card-list__title")
    for job in listings:
        try:
            print (job.text)
            print (job.get_attribute('href'))
            writer.writerow([job.text,"n/a","n/a",job.get_attribute('href')]) ##Filling in company and location later
            # t.sleep(1.0)
        except:
            pg=pg+1
            page[i+1].click()
            # t.sleep(2.0)
        # t.sleep(1.0)




t.sleep(6.0)
driver.quit()
file.close()
