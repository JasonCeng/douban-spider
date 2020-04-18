# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import time
import numpy as np
import urllib

# A function for setting HTTP headers
def setHeaders(url):
  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br', # if this line is added, the page will be garbled.
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'book.douban.com',
    'Referer': url,
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
  }
  return headers

# A function for setting HTTP Cookie
cookies = {
  'Cookie': 'bid=2PO7OVd5sWc; douban-fav-remind=1; gr_user_id=cec8f650-bd35-4d8e-b52a-908af08abc66; _vwo_uuid_v2=DA5BBA5297373253C99165C8D9860DE06|20f91a9d51e40dc02c2c20a2d9184730; __yadk_uid=humkmVsnKOx2JVlRHvKwM25r56J2LuSv; ll="118267"; douban-profile-remind=1; __utmv=30149280.13083; __gads=ID=67540cc11cc8fe4f:T=1562551755:S=ALNI_MYSyvT5hjeVW9G9qY4VDPq4KX8jgw; Hm_lvt_6e5dcf7c287704f738c7febc2283cf0c=1567376884; viewed="1924288_4707725_26150549_1088054"; push_noty_num=0; push_doumail_num=0; dbcl2="130831067:8Avh5J7mURs"; __utmz=30149280.1585660002.32.17.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ck=XifE; __utmc=30149280; __utmc=81379588; __utmz=81379588.1586533355.17.13.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doumail/; ap_v=0,6.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1586602897%2C%22https%3A%2F%2Fwww.douban.com%2Fdoumail%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.1033111501.1556794062.1586589473.1586602897.37; __utmt_douban=1; __utma=81379588.1818368698.1556794556.1586589473.1586602897.20; __utmt=1; __utmb=30149280.2.10.1586602897; __utmb=81379588.2.10.1586602897; _pk_id.100001.3ac3=bb4691241232828d.1556794558.18.1586602906.1586593510.'
}

# A function for setting HTTP paraMs
def setParams(offset_value):
  params = {
    'start': offset_value,
    'type': 'S',
  }

# A regular expression for \n \t \f \r
# |&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020 # Some white space ASCII CODE
res = re.compile(r'\n|\t|\f|\r')

# douban c++ book function
def doubanCPlusPlusFun():
  url = 'https://book.douban.com/tag/' + urllib.request.quote('C++') + '?start=0&type=S'
  headers = setHeaders(url)
  params = setParams(0)
  req = requests.post(url = url, headers = headers, params = params, cookies = cookies)
  req.encoding = 'utf-8'
  html = req.text # getting the request's result in text
  bf = BeautifulSoup(html, 'lxml') # useing BeautifulSoup to parsing page content with lxml rule
  paginator_div = bf.find_all('div', class_ = 'paginator') # useing bf's find_all method to find ul.subject-list
  a_bf = BeautifulSoup(str(paginator_div[0]), 'lxml')
  a = a_bf.find_all('a')
  page_list = [0]  
  a_len = len(a)
  for index in range(a_len):
    if index == a_len - 1:
      break;
    else:
      a_content = res.sub('', str(a[index].get_text())).strip()
      page_item = (int(a_content) - 1) * 20
      page_list.append(page_item)

  offset = page_list  # offset list for douban book C++ tag pages
  for offset_value in offset: # loop in every page
    url = 'https://book.douban.com/tag/' + urllib.request.quote('C++') + '?start=' + str(offset_value) + '&type=S' # building a url for current page
    headers = setHeaders(url) # setting HTTP headers
    params = setParams(offset_value) # settingHTTP params
    try:
      req = requests.post(url = url, headers = headers, params = params, cookies = cookies) # useing requests module's post method with some necessary parameters
      req.encoding = 'utf-8' # setting the requests result's encoding with utf-8
      html = req.text # getting the request's result in text
      bf = BeautifulSoup(html, 'lxml') # useing BeautifulSoup to parsing page content with lxml rule
      ul = bf.find_all('ul', class_ = 'subject-list') # useing bf's find_all method to find ul.subject-list

      h2_bf = BeautifulSoup(str(ul[0]), 'lxml') # build h2 element to bf object with lxml rule
      h2 = h2_bf.find_all('h2') # finding all h2 element to a list

      for item in h2: # loop h2 element list
        a_bf = BeautifulSoup(str(item),'lxml') # build a lemeent to bf object with lxml rule
        a = a_bf.find_all('a') # finding all a element to a list
        length = len(a) # a list length
        n = 0 # n for judge position in a list
        for item in a:
          n += 1
          clean_res = res.sub('', str(item.get_text())).strip() # clean the text in <a> element
          # print(item.findAll(text=True)) #This way is also fine
          print(clean_res) # print result
          with open('.\douban_c++_bookList.txt', 'a', encoding = 'utf8') as file_obj: # create a append model file objecft for file write, encoding with utf8
            if n == length-1: # judgeing if n is on last position of a list
              file_obj.write(clean_res) # if yes, not add \n
            else:
              file_obj.write(clean_res+'\n') # if not, add \n
      time.sleep(np.random.rand()*5) # sleep for a random time
    except:
      print('error')

# main function
if __name__ == '__main__':
  doubanCPlusPlusFun()