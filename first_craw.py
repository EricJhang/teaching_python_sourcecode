import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " ERROR "
res= get_html('https://www.ptt.cc/bbs/Food/index.html')
soup = BeautifulSoup(res,'lxml')
print(soup.prettify())


soup.find_all('a')
list_a=soup.find_all('a',class_="btn wide")
print(type(soup.find_all('a',class_="btn wide")))
print(list_a)
print(type(list_a))
list_a[0]['href']
tmp_html=list_a[1]['href'].split('/')
res_nextpage=get_html('https://www.ptt.cc/bbs/Food/'+tmp_html[-1])
soup_nextpage = BeautifulSoup(res_nextpage,'lxml')

res_nextpage=get_html('http://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx')
soup_nextpage = BeautifulSoup(res_nextpage,'lxml')
print(soup_nextpage.prettify())