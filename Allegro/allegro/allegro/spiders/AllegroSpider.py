
import scrapy

from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector
from scrapy.exceptions import DropItem

from allegro.items import AllegroItem

class AllegroSpider(SitemapSpider):
    name = 'allegro-spider'
    allowed_domains = ['allegro.pl']
    sitemap_urls = ['http://allegro.pl/robots.txt']
    sitemap_rules = [
        ('sportowe-nike', 'parse_nike'),
    ]
    def parse_nike(self, response):
        yield {
            'price': response.selector.xpath('//meta[@itemprop="price"]/@content').extract(),
            'title': response.selector.xpath('//meta[@itemprop="name"]/@content').extract(),
            'image': response.selector.xpath('//meta[@itemprop="image"]/@content').extract(),
            'url': response.selector.xpath('//meta[@itemprop="url"]/@content').extract()
        }