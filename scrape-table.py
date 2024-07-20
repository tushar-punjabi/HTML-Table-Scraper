import scrapy
 
 
class ScrapeTableSpider(scrapy.Spider):
    name = 'scrape-table'
    allowed_domains = ['https://getbootstrap.com/docs/4.0/content/tables']
    start_urls = ['http://https://getbootstrap.com/docs/4.0/content/tables/']
 
 
    def start_requests(self):
        urls = [
            'https://getbootstrap.com/docs/4.0/content/tables',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//*[@id="body-wrapper"]/main/div/div/div[10]/table/tbody/tr[1]'):
            yield {
                'first' : row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle' : row.xpath('td[3]//text()').extract_first(),
            }



            