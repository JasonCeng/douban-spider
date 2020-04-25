# douban-spider
对豆瓣网的计算机类书籍进行爬取和分析

## 爬取豆瓣书籍
C++作为一门伟大的语言，总是让人心生敬畏，作为本项目的开山之作，首先对<a href="https://book.douban.com/" target="_blank">豆瓣读书</a>上的C++标签的所有书籍进行爬取，目前只爬取了书名，并存储到txt文件中，后续会继续迭代，爬取书籍作者、译者、出版社、出版时间、价格等相关信息。

项目第二个版本开始支持输入书籍标签进行爬取，通过python参数传入。

## 版本详解
程序名 | 说明 
:- | :- 
douban_cplusplus_book_spider.py | 初代豆瓣爬虫版本，固定查询C++标签书籍，按评价排序（S），存储到txt文件中 
douban_book_spider.py | 第二代豆瓣爬虫版本，通过python参数控制查询书籍标签，按综合评价排序（T），存储到txt文件中

## 运行方式
```
git clone https://github.com/JasonCeng/douban-spider.git
cd douban-spider
python3 douban_cplusplus_book_spider.py
or
python3 douban_book_spider.py 数据库 [,计算机网络, Java, ...] --每次输入一个参数
```

## To-do-List
- [x] 爬取豆瓣读书C++书籍，存储到txt中 ```--douban_cplusplus_book_spider.py```
- [x] 支持输入自定义书籍标签进行爬取 ```--douban_book_spider.py```
- [ ] 支持csv存储
- [ ] 爬取书籍作者、译者、出版社、出版时间、价格
- [ ] 爬取书籍评分
- [ ] 爬取书籍封面