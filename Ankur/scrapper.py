import os
import time
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Open browser and get data
browser = webdriver.Firefox()

# Url from which i will get my data
myUrl = "http://vicepresidentofindia.nic.in/speeches-Interviews"
browser.get(myUrl)

'''#Todo
for i in range(0, 54):
    print(i)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    try:
        browser.find_element_by_class_name('pager-next').click()
    except:
        pass'''

'''HTML PARSING'''

# Parse html
page_soup = soup(browser.page_source, "html5lib")

'''Grab all speeches'''

containers = page_soup.find_all("div", {"class": "views-field views-field-title"})
print("Number of speeches found:: ", len(containers))

for contains in containers:
    #print(contains)
    try:
        product_page_link_container = contains.find('h3', {'class': 'field-content'})
        print(product_page_link_container)
        product_detail_url = product_page_link_container['href']
        newUrl = myUrl + product_detail_url
        print('adsfe')
        print(newUrl)

        openurl = uReq(newUrl)
        pageHtml = openurl.read()
        openurl.close()
        pageSoup = soup(pageHtml, 'html.parser')

    except:
        pass

print('Ankur Ranjan')