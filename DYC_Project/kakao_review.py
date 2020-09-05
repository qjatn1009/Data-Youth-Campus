import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import re
import pickle
import openpyxl 
import csv

loca_url = ['https://place.map.kakao.com/26874176#comment']
# max_sheet = 0
# filename = '서울위치.xlsx'
# wb = openpyxl.load_workbook(filename)
# df1 = pd.read_excel(filename, sheet_name = 1)
# # print(df1)
# sum = 0
# for i in range(len(df1)):
#     sum += int(df1['리뷰건수'][i][0])
#     if int(df1['리뷰건수'][i][0]) == 0 :
#         continue
#     else:
#         loca_url.append(df1['리뷰url'][i])
    #     sum += int(df1['리뷰건수'][i][0])
# print(sum)
# print(len(loca_url), sum)
review_result = []

def review_search(driver):  #url에서 리뷰 추출
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    reviews = bs.select('ul.list_evaluation > li')
    for review in reviews:
        list1 =[]
        if len(review.select(".num_rate")) == 0 :
            continue
        else:
            list1.append(int(review.select(".num_rate")[0].text[0]))
            if len(review.select(".txt_comment > span")) == 0:
                return 0
            list1.append(review.select(".txt_comment > span")[0].text)
            review_result.append(list1)
    
def get_review(url):
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    webdriver_options.add_argument('--disable-gpu')
    webdriver_options.add_argument('lang=ko_KR')
    driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe', chrome_options = webdriver_options)
    # driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe')
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    if len(bs.select("#mArticle > div.cont_evaluation > div.evaluation_sorting > a > span.color_b")) == 0:
        return 
    count = int(bs.select("#mArticle > div.cont_evaluation > div.evaluation_sorting > a > span.color_b")[0].text)
    if count % 25 == 0:
        pages = count // 25
        pages -= 1
    else:
        pages =count // 25
    count -= pages*25
    count //= 5
    count -= 1

    numbers =[3,4,5,6]
    for page in range(pages): 
        if review_search(driver) == 0:
            break 
        for i in numbers:
            number = "div.evaluation_review > div > a:nth-child({0})".format(i)
            driver.find_element_by_css_selector(number).click()
            time.sleep(1)
            review_search(driver)
        driver.find_element_by_css_selector("a.btn_next").click()
        time.sleep(1)
        numbers = [4,5,6,7]
    if pages == 0:
        numbers = [3,4,5,6]
    else:
        numbers= [4,5,6,7]
    if review_search(driver) == 0:
        return 0
    for i in range(count):
        number = "div.evaluation_review > div > a:nth-child({0})".format(numbers[i])
        driver.find_element_by_css_selector(number).click()
        time.sleep(1)
        review_search(driver)
            
def make_xlsx(location_Info):  #csv파일로 변환
    if len(location_Info) == 0:
        return
    filename = 'kakao_review.xlsx'
    # column = ['리뷰점수', '리뷰내용']
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    # ws.append(column)
    for review in location_Info:
        ws.append(review)
    wb.save(filename)

for i in range(0, 1):
    review_result = []
    get_review(loca_url[i])
    make_xlsx(review_result)
    print(i)
