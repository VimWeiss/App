import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class OnePageSpider(CrawlSpider):
    # name – имя паука
    name = "chgk_spider"
    # allowed_domains – домены сайта, в пределах которого необходимо сканировать
    allowed_domains = ["www.db.chgk.info"]
    # start_urls – список начальных адресов
    start_urls = ["https://db.chgk.info/tour/balkan23_u"]
    
    # rules - правила, определяющие поведение паука
    # первое правило: проваливаемся внутрь отзыва для того, чтобы достать заголовок и текст отзыва
    rules = (Rule(LinkExtractor(restrict_xpaths="//div"), callback='parse_item', follow = True),
            )
    def parse_item(self, response):
        item = {}
        item['question'] = response.xpath("//div[contains(@class, 'question')]/text()").get().strip()
        item['answer'] = response.xpath("//div[contains(@class, 'answer')]/text()").get().strip()
        return item