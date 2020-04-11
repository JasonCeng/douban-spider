# douban-spider
对豆瓣网的计算机类书籍进行爬取和分析

## 爬取豆瓣C++书籍
C++作为一门伟大的语言，总是让人心生敬畏，作为本项目的开山之作，首先对<a href="https://book.douban.com/" target="_blank">豆瓣读书</a>上的C++标签的所有书籍进行爬取，目前只爬取了书名，并存储到txt文件中，后续会继续迭代，爬取书籍作者、译者、出版社、出版时间、价格等相关信息。

## 运行方式
```
git clone https://github.com/JasonCeng/douban-spider.git
cd douban-spider
python douban_book_spider.py
```