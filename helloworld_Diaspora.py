from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

# Configure our web browser
options = webdriver.ChromeOptions()
#options.add_argument('headless');
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options)
# End web browser config

#Headless instatiation


driver.get('https://despora.de/stream')

time.sleep(3)

### Begin Actions
username = driver.find_element_by_css_selector("#user_username")
password = driver.find_element_by_css_selector("#user_password")
username.send_keys("johndoe" + Keys.TAB )
password.send_keys("maryhadalittlelamb" + Keys.ENTER)
#password.send_keys(u'\ue007')

driver.get('https://despora.de/stream')


time.sleep(10)

### BEGIN AUTOMATION

for i in range(1, 4):
    textbox = driver.find_element_by_css_selector("#status_message_text")
    textbox.send_keys("Hello, Hello testing with selenium, test %d " % (i))
    submitbutton = driver.find_element_by_css_selector("#submit").click()
    time.sleep(10)


#Write output to /tmp
driver.get('https://despora.de/stream')
with open("/tmp/source.html", "w") as f:
    f.write(driver.page_source)

#close the browser
driver.close()
print("I have closed the browser driver and posted your data, Master Russell.")

