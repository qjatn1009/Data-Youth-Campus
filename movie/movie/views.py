from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import naver_movie, naver_keyword
import requests
from bs4 import BeautifulSoup

# Create your views here.

def navermovie_star(request):
    qs = naver_movie.objects.all()
    qs.delete()
    result = crawling(1,2)
    
    for i in result:
        i.save()
    print('성공')
    return HttpResponseRedirect(reverse('main'))

def main(request):
    return render(request, 'main.html')

def resultmoive(request):
    qs = naver_movie.objects.all()
    context = {'movie_list': qs}
    return render(request, 'movie.html', context)

def keyword(request):
    qs = naver_keyword.objects.all()
    qs.delete()
    naver_keyword = request.POST['keyword']
    results = naver_search(naver_keyword, 1)
    for i in results:
        i.save()
    print('성공')
    return HttpResponseRedirect(reverse('main'))

def resultkeyword(request):
    qs = naver_keyword.objects.all()
    context = {'keyword_list': qs}
    return render(request, 'keyword.html', context)


def naver_search(search_word, pages = 1):
    results = []
    i=1
    for page in range(pages): 
        url = 'https://search.naver.com/search.naver?f=&fd=2&filetype=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&research_url=&sm=tab_pge&start={0}&where=webkr'.format(str(i))
        r = requests.get(url)
        bs = BeautifulSoup(r.text, 'html.parser')
        search_naver = bs.select('#elThumbnailResultArea > li')
        for result in search_naver:
            title = result.select('a', {'class':'title_link'})[0].text
            url = result.select('div.web_url > a.txt_url')[0].text
            summary = result.select('dd.sh_web_passage')[0].text
            qs = naver_keyword(title= title, URL = url, summary=summary)
            results.append(qs)
        i+=10
    return results

def crawling(m, n ): # m이상 n 이하 페이지 출력
    result=[]
    for i in range(m,n+1):
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page='+str(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, 'lxml')
        tables = bs.select('#old_content > table > tbody > tr')
        for tr in tables:
            tds = tr.select('td')
            if len(tds) != 3:
                continue
            point = tds[1].select('em')[0].text #밑에 꺼와 같은 일을 함
            movie = tds[1].select('a[href]')[0].text
            writer = tds[2].select('a')[0].text
            qs = naver_movie(nickname=writer, score = point, movie_name= movie)
            result.append(qs)
    print(result)
    return result