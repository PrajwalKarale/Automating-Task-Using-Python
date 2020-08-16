from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://www.gmail.com")
browser.implicitly_wait(60)
browser.maximize_window()
email = browser.find_element_by_name("identifier")
email.clear()
email.send_keys("prajwalkarale0508@student.sfit.ac.in")
# browser.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
browser.implicitly_wait(60)

browser.find_element_by_id('identifierNext').click()

password = browser.find_element_by_name("password").send_keys("08061999praj")

browser.find_element_by_id('passwordNext').click()

enter_code = browser.find_element_by_xpath('//*[@id=":jp"]').click()

browser.find_element_by_class_name('YK').send_keys('BECMPNA')

# //*[@id=":jp"]
# /html/body/div[24]/div[2]/input