import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)



driver.get("https://coinmarketcap.com/gainers-losers")
more_buttons = driver.find_elements_by_class_name("cmc-tab__trigger")


for x in range(len(more_buttons)):
	if more_buttons[x].is_displayed():
		driver.execute_script("arguments[0].click();", more_button[x])
		time.sleep(1)


page_source = driver.page_source


print(page_source)
