import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://db.chgk.info/tour/balkan23_u
#https://db.chgk.info/tour/chmok17_u
#https://db.chgk.info/question/balkan23_u.1/11

class ChgkSpider(CrawlSpider):
    name = 'chgk_spider'
    start_urls = ['https://db.chgk.info/']
    rules = (
        Rule(LinkExtractor(allow='tour')),
        Rule(LinkExtractor(allow='question'), callback='parse_items'),
        Rule(LinkExtractor(allow='answer'), callback='parse_items')
    )
    
    def parse_items(self, response):
        yield {
            'question':response.css('p::text').get().strip()
        }
