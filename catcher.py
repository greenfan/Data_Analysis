#!/usr/bin/python
#
#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from subprocess import PIPE, Popen
import time

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0].decode('utf-8').strip()




# Configure our web browser
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(options=options)
# End web browser config

#Headless instatiation


# write to this
asurls = open('/tmp/urls', 'r')



### Begin Actions
remainingcount = cmdline("cat /tmp/urls | wc -l")
print(remainingcount)
count = 1
actual_count = int(869)
for a in asurls:
    actual_count = actual_count + 1
    driver.get(a)
    page = BeautifulSoup(driver.page_source)
    MyFile = open('/tmp/{}.html'.format(actual_count), 'a')
    MyFile.write(str(page))
    count = count + 1
    print("wrote page {}".format(count))
    remaindercount = int(remainingcount) - int(count)
    print("remaining pages: {}".format(remaindercount))
    time.sleep(15)




print(page)

driver.close()


#for i in asurls:
#    print(i)
