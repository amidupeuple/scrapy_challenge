# -*- coding: utf-8 -*-

import scrapy

class CommentsSpider(scrapy.Spider):
    name = "comments"
    start_urls = [
        'http://www.dns-shop.ru/product/5d4994a37de23361/35-smartfon-dexp-ixion-es135-hit-4-gb-belyj/opinion/',
		'http://www.dns-shop.ru/product/2b2e199946d83361/35-smartfon-highscreen-pure-j-512-mb-cernyj/opinion/'
    ]

    def parse(self, response):
        for opinion in response.xpath('//div[@class="opinion-item"]'):
            yield {
                'rating': opinion.xpath(".//div[@class='product-item-rating rating']/@data-rating").extract_first(),
                'comment': opinion.xpath('.//li[./span/text()="Комментарий"]/span[@class="description-text"]/.').extract_first()
            }

        '''next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)'''