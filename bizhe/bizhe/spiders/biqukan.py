# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis import spiders


class BiqukanSpider(spiders.RedisSpider):
    name = 'biqukan'
    redis_key = "biqukan:start_urls"

    # allowed_domains = ['biqukan.com']
    # start_urls = ['https://www.biqukan.com/16_16857/']

    def parse(self, response):
        url = response.xpath('//dd/a/@href').extract()
        for i in url:
            new_url = response.urljoin(i)
            yield scrapy.Request(url=new_url, callback=self.art_text)

    def art_text(self, response):
        title = response.xpath('//div[@class="content"]/h1/text()').extract()
        content = response.xpath('//div[@class="showtxt"]/text()').extract()
        for i in title:
            with open(r"D:\敛财人生\%s.txt" % i, 'w', encoding='utf-8') as f:
                for j in content:
                    new_content = j.replace('\xa0' * 8, '\n')
                    f.write(new_content)
