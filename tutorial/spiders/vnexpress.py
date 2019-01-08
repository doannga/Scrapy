# -*- coding: utf-8 -*-
import scrapy
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
    	items = []
    	for title_new in response.xpath("//a[@title]").extract():
    	    item = crawlExpressItem()
    	    item['title'] = response.xpath("//a[@title]/text()").extract()
    	    items.append(item)
    	    return items
        pass
