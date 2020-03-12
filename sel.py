import time
from bs4 import BeautifulSoup

from selenium import webdriver
'''

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
'''
page_source = open('out.html', 'r').read()
soup = BeautifulSoup(page_source, 'html')

coins_selector = soup.find_all('tr', class_='cmc-table-row')

for i in coins_selector:
    coin_name = i.find('a').contents[0]
    coin_change = i.find('div', class_='cmc--change-positive').contents[0]
    print(coin_name)
    print(coin_change)
	
