
import scrapy

from scrapy.spiders import SitemapSpider
from scrapy.selector import Selector

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
            'title': response.css("title ::text").extract_first(),
            'url': response.url
        }