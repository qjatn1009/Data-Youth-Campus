import requests
import json
import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import pickle
import openpyxl

apiKey = '5f4076c674c97ee9f612217f9e843f6c'
word = "을지로3가 맛집"  
location_Info = []


def Coordinate_search(query):  #카카오맵에서 나온 주소를 좌표로
    url = "https://dapi.kakao.com/v2/local/search/address.json?page=1&size=10&query="+query
    header = {'Authorization' : 'KakaoAK ' + apiKey}
    data = []
    res = requests.get(url, headers=header)
    data = res.json()['documents']
    if len(data) == 0:
        x, y = '알수없음', '알수없음'
    else:
        x, y = data[0]["x"], data[0]["y"]
    return x, y

def loca_Info(driver): # 아래 숫자 버튼 클릭
    for i in range(1,6):
        site = '#info\.search\.page\.no' + str(i)
        html = driver.page_source
        bs = BeautifulSoup(html, 'lxml')
        if 'HIDDEN' in bs.select(site)[0]['class']:
            continue
        else:
            driver.find_element_by_css_selector(site).click()
            time.sleep(1)
            location(bs)

def location(bs): # 이름, 주소, 평점 추출
    entrie = bs.select('.placelist')[0]
    review = bs.select('.numberofscore')
    name = entrie.select('.link_name')
    address = entrie.select('div.addr > p:nth-child(1)')
    score = entrie.select('.numberofscore')
    for j in range(len(name)):
        list2 = []
        list2.append(name[j].text)
        list2.append(address[j].text)
        list2.append(score[j].text)
        list2.append(review[j]['href'])
        loca_x, loca_y = Coordinate_search(address[j].text)
        list2.append(loca_x)
        list2.append(loca_y)
        location_Info.append(list2)

def location_search(keyword): #카카오맵에서 검색
    driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe')
    url = "https://map.kakao.com/"
    driver.get(url)
    driver.find_element_by_class_name('coach_layer.coach_layer_type1').click()

    search_box = driver.find_element_by_css_selector('#search\.keyword\.query')
    search_box.send_keys(keyword)

    driver.find_element_by_id('search.keyword.submit').click()
    time.sleep(1)

    driver.find_element_by_css_selector('#info\.search\.place\.more').click()
    time.sleep(1)

    num = 1
    possible = True
    while possible:
        loca_Info(driver)
        driver.find_element_by_css_selector('#info\.search\.page\.next').click()
        next = '#info\.search\.page\.next'
        last = BeautifulSoup(driver.page_source, 'lxml').select(next)[0]['class']
        if 'disabled' in last:
            possible = False

    loca_Info(driver)

def csv(location_Info):  #csv파일로 변환
    filename = 'kakao_location.xlsx'
    column = ['이름', '주소', '리뷰건수','리뷰url','x좌표','y좌표']
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    sheet = wb.create_sheet(word)
    ws = wb[word]
    ws.append(column)
    for review in location_Info:
        ws.append(review)
    wb.save(filename)

location_search(word)
csv(location_Info)
