from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import pickle

driver = webdriver.Chrome('C:\WebDriver\chromedriver.exe')
driver.get('https://www.instagram.com/explore/tags/서울맛집/')
time.sleep(3)

login = driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
login.click()
time.sleep(2)

facebook_login = driver.find_element_by_class_name('KPnG0')
facebook_login.click()
time.sleep(2)

userid = driver.find_element_by_id('email')
userid.send_keys('maxha97@naver.com')
time.sleep(2)

password = driver.find_element_by_id('pass') 
password.send_keys('Ggmlnh')
time.sleep(2)

login_button = driver.find_element_by_id('loginbutton')
login_button.click()
time.sleep(2)

do_later = driver.find_element_by_class_name('aOOlW.HoLwm ')
do_later.click()
time.sleep(2)

word= '부산대톤쇼우'
driver.get('https://www.instagram.com/explore/tags/'+word+'/')
time.sleep(2)

def select_first(driver):
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
    data = [content, date, like, place, tags]
    return data 

def move_next(driver):
    right = driver.find_element_by_css_selector('._65Bje.coreSpriteRightPaginationArrow') 
    right.click()
    time.sleep(3)

select_first(driver) 
result = []
n = 1
for i in range(20):
    data = get_content(driver)
    print(data)
    result.append(data)
    n += 1
    time.sleep(2)
    move_next(driver)

column = ['내용', '날짜', '좋아요', '장소', '해시태그'] #csv로 생성
df = pd.DataFrame(result, columns = column)
df.to_csv('톤쇼우.csv', columns = column, header = True)

df = pd.read_csv('톤쇼우.csv')
df

with open('data.pickle', 'wb') as fw:
    pickle.dump(result, fw)

with open('data.pickle', 'rb') as fr:
    data_1 = pickle.load(fr)
    
print(data_1)


