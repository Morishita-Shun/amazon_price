import sys
import os
import csv
import urllib.request
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

###
# Example:
# sudo python amazonPrice.py "https://www.amazon.co.jp/~" productName
###

savePath = "/etc/AmazonPrice/"
url = ""
name = ""
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

if len(sys.argv) == 3:
    url = sys.argv[1]
    name = sys.argv[2]
else:
    print("Enter url:")
    url = sys.stdin.readline()
    print("Enter name:")
    name = sys.stdin.readline().strip()

fileName = name + ".csv"

if not os.path.isdir(savePath):
    os.mkdir(savePath)

tdatetime = dt.now()
strtime = tdatetime.strftime("%Y%m%d-%H%M%S")

request = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(request).read()

# soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "lxml")

data = soup.find("span", id="priceblock_ourprice")
price = data.text
price = price.replace("￥ ", "").replace(",", "")

f = open(savePath + fileName, "a")
writer = csv.writer(f)
array = []
array.append(strtime)
array.append(price)
writer.writerow(array)
f.close()
