from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pickle
import openpyxl

def read_File(filename):
    wb = openpyxl.load_workbook(filename)
    df1 = pd.read_excel(filename, sheet_name = 0)
    for i in range(len(df1)):
        name = df1["이름"][i].replace(" ", "")
        location_name.append(name)

def instagramLogin(driver):

    facebook_login = driver.find_element_by_class_name('KPnG0')
    facebook_login.click()
    time.sleep(1)

    userid = driver.find_element_by_id('email')
    userid.send_keys('maxha97@naver.com')
    time.sleep(1)

    password = driver.find_element_by_id('pass') 
    password.send_keys('Ggmlnh')
    time.sleep(1)

    login_button = driver.find_element_by_id('loginbutton')
    login_button.click()
    time.sleep(5)

    do_later = driver.find_element_by_class_name('aOOlW.HoLwm ')
    do_later.click()
    time.sleep(1)

def select_first(driver):
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    if len(bs.select('div._9AhH0')) == 0:
        return 0
    first = driver.find_element_by_css_selector('div._9AhH0') 
    #find_element_by_css_selector 함수를 사용해 요소 찾기
    first.click()
    time.sleep(3) #로딩을 위해 3초 대기

def get_content(driver):
    # 1. 현재 페이지의 HTML 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # 2. 본문 내용 가져오기
    try:  			#여러 태그중 첫번째([0]) 태그를 선택  
        content = soup.select('div.C4VMK > span')[0].text 
        			#첫 게시글 본문 내용이 <div class="C4VMK"> 임을 알 수 있다.
                                #태그명이 div, class명이 C4VMK인 태그 아래에 있는 span 태그를 모두 선택.
    except:
        content = ' ' 
    # 3. 본문 내용에서 해시태그 가져오기(정규표현식 활용)
    tags = re.findall(r'#[^\s#,\\]+', content) # content 변수의 본문 내용 중 #으로 시작하며, #뒤에 연속된 문자(공백이나 #, \ 기호가 아닌 경우)를 모두 찾아 tags 변수에 저장
    # 4. 작성 일자 가져오기
    try:
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10] #앞에서부터 10자리 글자
    except:
        date = ''
    # 5. 좋아요 수 가져오기
    try:
        like = soup.select('div.Nm9Fw > button')[0].text[4:-1] 
    except:
        like = 0
    # 6. 위치 정보 가져오기
    try:
        place = soup.select('div.JF9hh')[0].text
    except:
        place = ''
    if 2015 <= int(date[:4]) <= 2020:
            data = [content, date, like, place, tags]
            return data
    else:
        return []

def move_next(driver):
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    if len(bs.select('._65Bje.coreSpriteRightPaginationArrow')) == 0:
        return 0
    right = driver.find_element_by_css_selector('._65Bje.coreSpriteRightPaginationArrow') 
    right.click()
    time.sleep(3)

def make_pickle(name, data):
    if len(data) == 0:
        return 
    with open(name+".pickle", 'wb') as fw:
        pickle.dump(data, fw)

def x_Btn(driver):
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')
    if len(bs.select("div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button")) == 0:
        return 0
    driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > button").click()
    time.sleep(1)

driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe')
driver.get('https://www.instagram.com/')
time.sleep(1)
location_name = []
result = []

read_File("을지로.xlsx")
instagramLogin(driver)
for num in range(16, len(location_name)):
    result = []
    name = location_name[num].replace(" ", "")
    driver.get('https://www.instagram.com/explore/tags/'+name+'/')
    time.sleep(2)
    if select_first(driver) == 0:
        continue
    while True:
        data = get_content(driver)
        if len(data) == 0:
            break
        else:
            result.append(data)
        time.sleep(2)
        if move_next(driver) == 0:
            break
    make_pickle(name ,result)
    print(num, "번 성공")
    if x_Btn(driver) == 0:
        pass


# def read_pickle(filename):
#     with open(filename, 'rb') as fr:
#         data_1 = pickle.load(fr)
#         return data_1

# def make_pickle(name, data):
#     if len(data) == 0:
#         return 
#     with open(name+".pickle", 'wb') as fw:
#         pickle.dump(data, fw)