import time

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/home/kali/Downloads/chromedriver", chrome_options=options)



driver.get("https://coinmarketcap.com/gainers-losers")



#more_buttons = driver.find_elements_by_class_name("cmc-tab__trigger")

Hourbutton = driver.find_elements_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[2]/ul[1]/li[1]")

print(Hourbutton)

#print(more_buttons)


for x in range(len(Hourbutton)):
	if Hourbutton[x].is_displayed():
		driver.execute_script("arguments[0].click();", Hourbutton[x])
		time.sleep(1)



page_source = driver.page_source

print(page_source)

