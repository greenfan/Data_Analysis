#!/usr/bin/python3


from bs4 import BeautifulSoup
import requests

result =  requests.get("https://coinmarketcap.com/gainers-losers/")

c = result.content


soup = BeautifulSoup(c)

hourdiv = soup.find(class_='cmc-tabs__body')


hourdivas = hourdiv.find_all('a')

for i in hourdivas:
	print(i)
	print("")
