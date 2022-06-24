import scrapy

class JuiceSpyder(scrapy.Spider):
    name = 'juiceshop'
    allowed_domains = ['juiceshop.com/']
    start_urls = ['https://juiceshop.com']

    def parse_product(self, response):
        products = response.xpath('//*[@class="product-wrap"]')
        
        title = products.xpath('//*[@class="product-thumbnail__title"]/text()').extract()
        price = products.xpath('//*[@class="money"]/text()').extract()

        for i in range(len(title)):
            yield {'Title': title[i], 'Price': price[i]}

    def start_requests(self):
        url = 'https://juiceshop.com/collections/food'
        yield scrapy.Request(url=url, callback=self.parse_product)