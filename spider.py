# -*- coding: utf-8 -*-

import scrapy
import re

class CommentsSpider(scrapy.Spider):
    name = "spider_dns_shop"
    
    #this is url which will be concatenated with particular brand
    brand_url = "http://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/?brand="
    
    start_urls = [
        'http://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/'
    ]

    
    def parse(self, response):
        print("@@@: response url: " + response.url)
        
        if "http://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/" == response.url:
            #This is initial if - we will get here only at first time when origin response will be returned
            #The goal - prepare all urls for available brands
            brand_div = response.xpath("//div[@data-id='brand']")
            brands_list = brand_div.xpath(".//div[@data-role='filter-block-item']/input[@type='checkbox']/@data-id").extract()
            for b in brands_list:
                b_url = self.brand_url + b
                yield response.follow(b_url, self.parse)
        elif "brand" in response.url:
            #Here we go when response with particular brand is returned
            #Goal - prepare urls for all products
            for item in response.xpath("//a[@class='show-popover ec-price-item-link image-container']/@href").extract():
                if item is not None:
                    item_url = re.sub("\?(.*)", "opinion/", item)
                    print("@@@: product url: " + item_url)
                    yield response.follow(item_url, self.parse)
        elif "product" in response.url:
            for opinion in response.xpath('//div[@class="opinion-item"]'):
                if opinion:
                    yield {
                        'rating': opinion.xpath(".//div[@class='product-item-rating rating']/@data-rating").extract_first(),
                        'comment': opinion.xpath('.//li[./span/text()="Комментарий"]/span[@class="description-text"]/.').extract_first()
                    }
            
                next_list = response.xpath("//li[@class='next']")
                if len(next_list) > 0:
                    next = next_list[0]
                    next_url = next.xpath(".//a/@href").extract_first()
                    if next_url is not None:
                        print("@@@: comment url: " + next_url)
                        yield response.follow(next_url, self.parse)
