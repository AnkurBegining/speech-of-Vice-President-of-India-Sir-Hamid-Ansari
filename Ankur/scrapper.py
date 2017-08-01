import os
import time
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Open browser and get data
browser = webdriver.Firefox()

# Url from which i will get my data
myUrl = "http://vicepresidentofindia.nic.in/speeches-Interviews"
MyUrl = "http://vicepresidentofindia.nic.in"
browser.get(myUrl)

m=1
for i in range(0, 54):
    print(i)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    '''HTML PARSING'''

    # Parse html
    page_soup = soup(browser.page_source, "html5lib")

    '''Grab all speeches'''

    containers = page_soup.find_all("div", {"class": "views-field views-field-title"})
    print("Number of speeches found:: ", len(containers))

    for contains in containers:
        # print(contains)
        try:
            product_page_link_container = str(contains.find('a'))
            # print(product_page_link_container)
            product_detail_url = product_page_link_container[9:(product_page_link_container.index('>') - 1)]
            print(MyUrl + product_detail_url)
            desiredUrl = MyUrl + product_detail_url
            openurl = uReq(desiredUrl)
            pageHtml = openurl.read()
            openurl.close()
            pageSoup = soup(pageHtml, 'html.parser')

            ContainersForModel = pageSoup.find('h1', {'class': 'page__title title'}).getText()
            ModelNumber = ContainersForModel.strip()
            print(ModelNumber)
            ContainerForSpeechText = pageSoup.find('div', {'class': 'views-field views-field-body'}).getText()
            print(ContainerForSpeechText)

            saveFile = open('Speech{}.txt'.format(m), 'w')
            saveFile.write(ContainerForSpeechText)
            saveFile.close()
            m = m + 2


        except:
            pass

    try:
        browser.find_element_by_class_name('pager-next').click()
    except:
        pass

print('Ankur Ranjan')