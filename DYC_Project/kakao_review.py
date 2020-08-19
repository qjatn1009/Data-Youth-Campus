import requests
import json
import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pickle
import openpyxl 

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
            list1.append(review.select(".txt_comment > span")[0].text)
            review_result.append(list1)
    
def get_review(url): 
    driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe')
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')

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
        review_search(driver) 
        for i in numbers:
            number = "div.evaluation_review > div > a:nth-child({0})".format(i)
            driver.find_element_by_css_selector(number).click()
            time.sleep(1)
            review_search(driver)
        driver.find_element_by_css_selector("a.btn_next").click()
        time.sleep(1)
        numbers = [4,5,6,7]

    numbers= [4,5,6,7]
    review_search(driver)
    for i in range(count):
        number = "div.evaluation_review > div > a:nth-child({0})".format(numbers[i])
        driver.find_element_by_css_selector(number).click()
        time.sleep(1)
        review_search(driver)
            
def csv(location_Info):  #csv파일로 변환
    filename = 'kakao_review.xlsx'
    # column = ['리뷰점수', '리뷰내용']
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    # ws.append(column)
    for review in location_Info:
        ws.append(review)
    wb.save(filename)

get_review("https://place.map.kakao.com/8332362#comment")
csv(review_result)