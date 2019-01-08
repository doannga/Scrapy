# -*- coding: utf-8 -*-
import scrapy
# cái này lỗi vì trong tutorial, file items không có lớp crawlExpressItem
from tutorial.items import crawlExpressItem

class VnexpressSpider(scrapy.Spider):
    name = 'vnexpress'
    allowed_domains = ['vnexpress.net']
    start_urls = ['http://vnexpress.net/']
    def start_requests(self):
    	for url in self.start_urls:
    		yield scrapy.Request(url = url, callback = self.parse)
    	pass
    def parse(self, response):
        #response.xpath("//a[@title]").extract() có phải 1 list k?
    	for title_new in response.xpath("//a[@title]").extract():
            # định nghĩa lại crawlExpressItem() đi nhé
    	    item = crawlExpressItem()
    	    item['title'] = response.xpath("//a[@title]/text()").extract()
    	    return item
        pass
