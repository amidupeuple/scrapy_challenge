# -*- coding: utf-8 -*-

import scrapy

from scrapy.exporters import JsonLinesItemExporter
class MyJsonLinesItemExporter(JsonLinesItemExporter):
    def __init__(self, file, **kwargs):
        super(MyJsonLinesItemExporter, self).__init__(file, ensure_ascii=False, **kwargs)




class CommentsSpider(scrapy.Spider):
    name = "comments"
    start_urls = [
        'http://www.dns-shop.ru/product/c80996e14c028d95/4-smartfon-dexp-ixion-e240-strike-2-8-gb-cernyj/opinion/',
    ]

    def parse(self, response):
        for feedback in response.xpath('//li[./span/text()="Комментарий"]/span[@class="description-text"]/text()').extract():
            
            yield {
                'comment': feedback
            }

        '''next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)'''