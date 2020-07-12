#!/usr/bin/python
import feedparser
from datetime import datetime
from selenium import webdriver
import time
import re

from selenium.webdriver.common.keys import Keys



url = "https://zapier.com/engine/rss/7955983/OpenScienceRSS"
NewsFeed = feedparser.parse(url)



# Configure our web browser
options = webdriver.ChromeOptions()
#options.add_argument('headless');
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options)
# End web browser config

#Headless instatiation





driver.get('https://diasp.org/stream')

time.sleep(3)

### Begin Actions
username = driver.find_element_by_css_selector("#user_username")
password = driver.find_element_by_css_selector("#user_password")
username.send_keys("helloWorld" + Keys.TAB )
password.send_keys("wouldn'tyoulinke2know" + Keys.ENTER)

driver.get('https://diasp.org/stream')

time.sleep(15)


textbox = driver.find_element_by_css_selector("#status_message_text")

todays_date = format(datetime.today().day).zfill(2)
print(todays_date)
### Begin action



a_count = len(NewsFeed.entries)
print(a_count)
t_count = 0
print("T count {}".format(t_count))
for i in range(0, a_count):
    entry = NewsFeed.entries[i]
    pdate = entry.published.split()
    if todays_date in pdate[1]:
        t_count = t_count + 1
        print(entry.published)



print("total_new_stories from {} is {}".format(todays_date,t_count))



for i in reversed(range(0, t_count)):
    entry = NewsFeed.entries[i]
    pdate = entry.published
    textbox.send_keys('#### {0}\n****\n'.format((entry.title)))
    time.sleep(0.5)

    try:
        hashtags = entry.author
        hashtags2 = re.sub("[ ]", ",", hashtags)
        hashlist = re.split(',', hashtags2)
    except AttributeError:
	hashlist = [ "insert_hashtags" ]

    hash = ['#' + i for i in hashlist]
    stop_words = ["#&", "#and", "#", "#with", "#the"]
    fullhash = list(set(filter(lambda w: w not in stop_words, hash)))
    print(*fullhash)
    textbox.send_keys('> {0}\n {1} \n {2} \n ****'.format(entry.summary,entry.link,', '.join(fullhash)))
    time.sleep(1)
    submitbutton = driver.find_element_by_css_selector("#submit").click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    time.sleep(900)



driver.close()
print("...")
time.sleep(1)
print("I have typed it and clicked submit, Master.")




