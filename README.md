

#关于笔趣看小说网的爬取

#采用scrapy-redis分布式爬取，能在极短时间内完成数据的采集。

# start_urls = ['https://www.biqukan.com/16_16857/'] 

#该url是关于<敛财人生>这本小说的地址，如需要其他小说爬取，只需更换url即可。

#关于数据的采集是利用scrapy框架本身的xpath解析，从而提取数据

#  for j in content:   new_content = j.replace('\xa0' * 8, '\n')

#  用于清洗提取出来的小说内容中的空格



