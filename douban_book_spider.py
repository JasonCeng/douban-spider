# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re

headers = {
    'Cookie':'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
# &nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020
res = re.compile(r'\n|\t|\f|\r|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020')

if __name__ == '__main__':
  target = 'https://book.douban.com/tag/C++?start=&type=T'
  req = requests.post(url = target, headers = headers)
  html = req.text
  bf = BeautifulSoup(html, 'lxml')
  ul = bf.find_all('ul', class_ = 'subject-list')

  h2_bf = BeautifulSoup(str(ul[0]), 'lxml')
  h2 = h2_bf.find_all('h2')

  for each in h2:
    a_bf = BeautifulSoup(str(each),'lxml')
    a = a_bf.find_all('a')
    # print(a)
    for each in a:
      clean_res = res.sub('', str(each.get_text()))
      # print(each.findAll(text=True))
      print(clean_res)