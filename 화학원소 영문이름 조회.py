import time
from selenium import webdriver
import xlrd
from xlutils.copy import copy
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import os

results = []
# driver
driver = webdriver.Chrome(executable_path="/Users/user/Desktop/PYTHON/chromedriver_win32/chromedriver")

for i in range(1,101):
    driver.get("https://ko.wikipedia.org")

# 엑셀 파일 열기
    wb = xlrd.open_workbook('/Users/user/Desktop/화학.xlsx')
    sheet = wb.sheet_by_index(0)
# 검색 키워드 셀에서 가져오기
    song = sheet.cell(i, 1).value
    keyword = str(song) #숫자인 경우가 있어서 str()

    driver.implicitly_wait(1)

    try :
        elem = driver.find_element_by_xpath('//*[@id="searchInput"]') 
        elem.send_keys(keyword)
        elem.submit()
        driver.implicitly_wait(5)
        Latinname = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[3]/td').text 
        results.append(Latinname)
    except NoSuchElementException:
        print(" [예외 발생] 표 없음 ")
        results.append("")
        continue
import pandas as pd

dataframe = pd.DataFrame(results)

dataframe.to_csv("/Users/user/Desktop/namsu.csv",
                 header=False, index =False)
