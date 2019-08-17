# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request

url = "https://movie.douban.com/subject/26425063/ "
req = request.Request(url)
f = request.urlopen(req)   # Get该网页从而获得该html内容
result = f.read()
soup = BeautifulSoup(result)


fw = open('douban_movie.txt', 'w')
fw.write('description')
# <span property="v:summary" class="">
k = soup.find_all("span", attrs={"property": "v:summary"})[0].get_text()
if k is None:
    pass
else:
    print(k)
    fw.write(k)

fw.close()
