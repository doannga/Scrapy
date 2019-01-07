import scrapy
class quotes_spider(scrapy.Spider):
	name = "quotes"
	"""docstring for quotes_spider"""
	def start_requests(self):
		urls =[
			'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)
			# pass
		# pass
	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = "quotes-%s.html" %page
		with open(filename, "wb") as file:
			file.write(response.body)
			self.log('Save file %s' %filename)
			# pass
	
		