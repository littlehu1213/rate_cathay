from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup


def cathay(month):
    driver=webdriver.Chrome(executable_path="C:/Users/littlehu1213/chromedriver.exe")  #("c:/Users/user/chromedriver.exe")
    driver.get("https://www.cathaylife.com.tw/cathaylife/services/info/rate-index/rate")
    s1 = Select(driver.find_element_by_id('layout_0_rightcontent_0_category'))
    s1.select_by_index(1)
    sleep(3)
     
     
    s3 = Select(driver.find_element_by_id('layout_0_rightcontent_0_year'))
    s3.select_by_index(1)
    s4 = Select(driver.find_element_by_id('layout_0_rightcontent_0_month'))
    s4.select_by_index(2)
    bs=BeautifulSoup(driver.page_source,"html.parser")
    pages=bs.find_all(class_='w_220 productName')
    pages=pages[0].find_all('option')
    pages=str(pages)
    counts=pages.count('value')

    for i in range(1,counts):
        s2 = Select(driver.find_element_by_name('layout_0$rightcontent_0$productName'))
        s2.select_by_index(i)
        element = driver.find_element_by_id('productSearch')
        driver.execute_script("arguments[0].click();", element)
        sleep(1)
        bs=BeautifulSoup(driver.page_source,"html.parser")
        
        title=bs.find_all(class_="title-article-light")[1].string
        if(title.find('查無資料。')==0):
            print('error:'+title)
        else:
            bs=BeautifulSoup(driver.page_source,"html.parser")
            rate=bs.find_all(class_="basic")
            rate=rate[1].find_all('td')[2].string
            print(title+";"+rate)
    driver.close()


cathay(2)