#importing the necessary library..
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.gmail.com")
browser.implicitly_wait(60)
browser.maximize_window()

email = browser.find_element_by_name("identifier")
email.clear()
email.send_keys("")

# browser.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
browser.implicitly_wait(60)

browser.find_element_by_id('identifierNext').click()

password = browser.find_element_by_name("password").send_keys("")

browser.find_element_by_id('passwordNext').click()

#to open the meet dialog box.
enter_code = browser.find_element_by_xpath('//*[@id=":jp"]').click()

meeting_code = input('ENTER THE MEETING CODE: ')

#to type the meeting code.
browser.find_element_by_class_name('YK').send_keys(meeting_code)

#to click the JOIN button.
browser.find_element_by_xpath('/html/body/div[23]/div[3]/button').click()
