from selenium import webdriver
import time, subprocess


def main():

    # You most certainly want to change this
    url = "https://notabug.io/t/coronavirus/comments/12b46c06e792905c22844dd6d9c64efdfa030df7/its-frightening-doctors-say-half-of-cured-covid-patients-still-suffer"

    profile = webdriver.FirefoxProfile()
    # Set a user agent string to help parse webserver logs easily
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium.py")
    browser = webdriver.Firefox(profile)
    browser.get(url)
    time.sleep(10)
    clickbutt = browser.find_element_by_css_selector("div.arrow:nth-child(5)").click()






if __name__ == '__main__':
    main()