from django.shortcuts import render
from .models import User, seomyeon
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.
count,sentiment = 0, 1

def login_view(request):
    if request.method == "POST":
        name = request.POST["username"]
        passkey = request.POST["password"]
        if passkey == User.objects.get(user_id = name).pw:
            print("성공")
            return HttpResponseRedirect(reverse('map'))
        else:
            print("실패")
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'login.html')

def map(request):
    page = request.GET.get('page', 1)
    if request.method == "POST":
        qs = []
        # if request.POST["feeling"]:
        feeling = request.POST["feeling"]
        # else:
            # feeling = float(request.POST["surprised"])+float(request.POST["happy"])
        if float(feeling) >0.8:
            ranks=[ "서면더토닥","북카페심심푸리","서면비밀정원","녹아들다녹카페","서면유동커피","모던블루커피","고품격커피공장서면중앙점","샐리의아침","다트프린스서면점",
            "더달아서면","서면웨스트우드","19티서면","비트포비아서면","앨리스타로","반디트리","서면뉴욕보틀","망원동티라미수전포카페거리점","서면흑운당","라데세르",
            "서면연운당","서면심리카페멘토","서면라이츠커피","인레스트카페","서면어썸","서면델리케이트","고유커피로스터스부산서면점","서면듀랩","서면게임오브마인드","서면빈티지38",]
        elif 0.7 < float(feeling) <= 0.8:
            ranks = ['다트프린스서면점', '서면빈티지38', '서면흑운당', '서면설빙', '프리아트', '서면백금당', '서면하이안', '망원동티라미수전포카페거리점', '앨리스타로', 
            '카페안에사주와타로', '주스탐', '카페두오모', '더달아서면', '로드209', '비트포비아서면', '카페가지가지', '서면공차', '19티서면', 
            '서면심리카페멘토', '서면뉴욕보틀', '서면덕수네', '서면비포선셋', '카페비835', '서면플라스틱', '서면투썸플레이스', '서면러브썸', 
            '비브레이브서면', '까페코히', '카반에스프레소', '달구나카페', '갤러리아트카페', '서면어썸', '컬쳐컴플렉스', '고품격커피공장서면중앙점', 
            '큐식이네', '서면마틴커피로스터스', '서면조딥', '샐리의아침', '삐에로보드게임', '서면분커', '트모르', '커피스놉', '서면카페더맨션', 
            '서면블랙업', '서면안티크', '서면오소39', '서면어슬로우데이', '월하객잔', '서면롶속', '서면돈두커피'] 
        elif 0.5 < float(feeling) <= 0.7:
            ranks = ["주스탐","브라운웍스","서면랑데자뷰","서면이너프","애블유","서면공차","다트프린스서면점","서면투썸플레이스",
            "더달아서면","컬쳐컴플렉스","녹아들다녹카페","서면블랙업","앨리스타로","모던블루커피","카페안에사주와타로","서면버터럽",
            "서면어썸","인레스트카페","서면굿굿웨더","서면빽다방","고품격커피공장서면중앙점","테이블매스","비트포비아서면","서면공전상가","로스노비오스카페","스타벅스서면","서면브루스","서면카페더맨션","서면안티크","서면파스구찌",]
        elif 0.4 < float(feeling) <= 0.5:
            ranks = ['카반에스프레소', '19티서면', '서면랑데자뷰', '서면빽다방', '비브레이브서면', '달구나카페', '컬쳐컴플렉스', '녹아들다녹카페',
             '서면블랙업', '앨리스타로', '망원동티라미수전포카페거리점', '서면웨스트우드', '서면더토닥', '서면설빙', '서면연운당', '주스탐', '서면커피스미스', 
             '카페비835', '서면러브썸', '서면롶속', '서면굿굿웨더', '트모르', '서면마틴커피로스터스', '프리아트', '서면듀랩', '서면델리케이트', '타이디룸카페', 
             '덱스커피전포점', '서면유동커피', '서면카페모멘트']
        elif 0.3 < float(feeling) <= 0.4:  
            ranks = ["서면게임오브마인드","다트프린스서면점","서면백금당","샐리의아침","서면랑데자뷰","북카페심심푸리","서면랜드마크9","서면블랙업","카페안에사주와타로","서면이터널선샤인","서면어썸",
            "서면빈티지38","카페가지가지","더달아서면","카페두오모","달구나카페","서면투썸플레이스","프리아트","서면경성아가씨","요거트팡","애블유","서면돈두커피",
            "녹아들다녹카페","서면문라운지","서면플라스틱","서면기븐","라데세르","서면노베이커노베이커스","월하객잔","서면뉴욕보틀"]
        elif float(feeling) <= 0.3:
            ranks = ["비트포비아서면","컬쳐컴플렉스","로드209","서면블랙업","고품격커피공장서면중앙점","카페가지가지","젤리죔죔","망원동티라미수전포카페거리점","반디트리","서면마틴커피로스터스","서면더토닥","서면공차",
            "비브레이브서면","브라운웍스","주스탐","서면심리카페멘토","스타벅스서면","서면비포선셋","서면랜드마크9","카페두오모","서면돈두커피","서면덕수네","인레스트카페","서면기븐","서면투썸플레이스","서면카페더맨션","샐리의아침","서면브루스","달구나카페"]
        
        for rank in ranks:
            seomyeon.objects.values_list
            lists = seomyeon.objects.get(search_word = rank)
            qs.append(lists)
        paginator = Paginator(qs, 10)
        store_info = paginator.get_page(page)
    else:
        page = request.GET.get('page', 1)
        qs = seomyeon.objects.all()
        paginator = Paginator(qs, 10)
        store_info = paginator.get_page(page)

    context = {'store_info' : store_info}
       
    return render(request, 'maps.html', context)
        # user_info = User.objects.get(username = username)
    # login_user = {"user" : user_info}
    # return render(request, 'kakaomap.html')