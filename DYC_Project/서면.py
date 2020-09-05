import requests
import json
import csv
import pandas as pd
from selenium import webdriver


result = []
name_list = ['서면블랙업', '서면브룩스', '서면카페모멘트', '카반에스프레소', '서면넉아웃', 
    '모리도중카페', '서면모던테이블', '서면옵포드', '서면문라운지', '서면공간', '비트포비아서면',
    '서면투썸플레이스', '여우별룸카페', '서면설빙', '스타벅스서면', '타이디룸카페', '서면게임오브마인드',
    '서면비밀정원', '프띠르마카롱', '서면에티오피아', '서면달콤커피', '서면공차', '북카페심심푸리', 
    '서면빽다방', '서면랑데자뷰', '19티서면', '앨리스타로', '양이양이고양이cafe', '카페북가든', '더달아서면',
    '고품격커피공장서면중앙점', '샐리의아침', '다트프린스서면점', '컬쳐컴플렉스', '삐에로보드게임', '와우와플', 
    '주스탐', '서면더토닥', '반디트리', '카페베르사유', '서면브루스', '큐식이네', '마녀의지팡이', '카페두오모', 
    '마피아주스', '서면도시농가코페', '서면마틴커피로스터스', '서면스쿱', '카반에스프레소서면', '프리아트', 
    '모던테이블서면점', '경성코페서면', '서면유동커피', '카페가지가지', '서면챔피언',  '카페q', '파파커피', 
    '로반스윗', '덕수네고양이카페', '젤리죔죔','서면비포선셋', '서면빈티지38', '서면FM커피하우스', '서면돈두커피', 
    '서면유동커피', '서면랜드마크9', '서면연운당', '서면굿굿웨더','망원동티라미수전포카페거리점', '서면다운트', '서면라이츠커피', 
    '메종지미지니팍', '서면북그러움', '서면노베이커노베이커스', '서면커피스미스','서면컬렉션', '서면어슬로우데이', '서면롶속', 
    '서면2인칭시점', '서면덕수네', '서면로망34', '서면델리케이트', '서면조딥', '서면웨스트우드','카페메인', '서면기븐', 
    '서면파스구찌', '서면DALA', '서면경성아가씨', '서면러브썸', '비트포비아서면', '서면오소39', '카페안에사주와타로',
    '서면듀랩', '서면카페더맨션', '서면흑운당', '서면숩65', '애블유', '고유커피로스터스부산서면점', '서면공전상가', '덱스커피전포점', '서면하이안',
    '로스노비오스카페', '비브레이브서면', '서면던다스', '서면심리카페멘토', '서면뉴욕보틀', '테이블매스', '브라운웍스', '로드209', '카페비835', 
    '요거트팡', '트모르', '카페인생상담', '모던블루커피', '엠케이브라운', '갤러리아트카페', '서면커먼가든', '커피스놉', '까페코히',
    '서면백금당', '서면이터널선샤인', '서면이너프', '서면모모치', '서면플라스틱', '로우앤스윗카페', '서면샬롯', '녹아들다녹카페', 
    '서면분커', '요소이요','서면버터럽', '월하객잔', '인레스트카페', '달구나카페', '서면어썸', '서면안티크', '서면코지타운', '서면연의양과',
    '라데세르', '메르시713','쉼표하나서면점', '제이브루스카페', '쎄투부산',"동래스타벅스","동래할리스커피", "동래골드스푼", "동래투썸플레이스",
    "티앤북스동래점", "코비스커피타임", "동래비커피", "어벤더치동래점","북카페심심푸리동래", "하이오커피동래점", "지프랭크커피", "더덤", 
    "동래초콜렛", "동래비커피", "대동커피숍", "카페포차"]

apiKey = '5f4076c674c97ee9f612217f9e843f6c' 

def search_keyword(keyword):  #카카오맵에서 나온 주소를 좌표로
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy&query="+keyword
    header = {'Authorization' : 'KakaoAK ' + apiKey}
    data = []
    res = requests.get(url, headers=header)
    data = res.json()['documents']
    if len(data) == 0:
        return 0
    place_name = data[0]["place_name"]
    category_name = data[0]["category_name"]
    place_url = data[0]["place_url"]
    x = data[0]["x"]
    y = data[0]["y"]
    return place_name, category_name, place_url, x, y

for name in name_list:
    place_info = []
    if search_keyword(name) == 0:
        continue
    place_name, category_name, place_url, x, y =search_keyword(name)
    place_info.append(place_name)
    place_info.append(category_name)
    place_info.append(place_url)
    place_info.append(x)
    place_info.append(y)
    place_info.append(name)
    result.append(place_info)

print(len(name_list), len(result))
column = ['이름', '카테고리', 'url','위도','경도',"검색어"]
df = pd.DataFrame(result, columns = column)
df.to_csv('서면카페.csv', columns = column, header = True)

df = pd.read_csv('서면카페.csv')
df