# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from Nike.items import NikeLink
from Nike.items import NikeShoe
from Nike.items import obiekt

# klasa definiujaca spidera i jego zachowanie
class NikeSpider(scrapy.Spider):
    name = "NikeSpider"
    allowed_domains = ["store.nike.com"]
    start_urls = [
        "http://store.nike.com/gb/en_gb/pw/mens-shoes/7puZoi3"
    ]

    # w przypadku poprawnej odpowiedzi wypisanie w logu jego adresu
    # extract określonych danych(nazwa,cena)
    def parse(self, response):
        self.logger.info('Uzyskano odpowiedz od serwera %s.', response.url)
        for href in response.xpath('.//div[@class="grid-item-image-wrapper sprite-sheet sprite-index-0"]'):
            links = href.xpath('normalize-space(a/@href)').extract()
            self.logger.info
            for link in links:
                self.logger.info('LINK: ')
                print link
                request = scrapy.Request
                yield scrapy.Request(link, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        #self.logger.info('Obiekt ze strony: ')
        #print response.url
        item = NikeShoe()
        names = response.xpath('normalize-space(//h1/text())').extract()
        prices = response.xpath('normalize-space(//span[@itemprop="price"]/text())').extract()
        for name in names:
            for price in prices:
                name = name.lstrip('u\'')
                price = price.lstrip('u\'\\xa')

                if name and price:
                    item['name'] = name
                    item['price'] = price
                    item['link'] = response.url
                    yield item


        """
        divs = response.xpath('//div')
        for p in divs.xpath('.//p'):
            print p.extract()   /
        """

        """
        produkty = response.xpath('.//div[@class="grid-item-info"]/p    ').extract()
        print produkty

        for produkt in produkty:
            item = obiekt()
            item['name'] = produkt.xpath('normalize-space(a[@class = "./product-name/text())').extract()
            item['price'] = produkt.xpath('normalize-space(a[@class = "./prices/text())').extract()
            yield item
        """
        """
                linki = response.xpath('normalize-space(//div[@class="grid-item-image-wrapper sprite-sheet sprite-index-0"]/a/@href)')
        """

# w przypadku poprawnej odpowiedzi wypisanie w logu jego adresu
# extract określonych danych(nazwa,link,opis) -- działa w przypadku alloweddomains i start urls store.nike.com/gb/en_gb
"""
    def parse(self, response):
        self.logger.info('Uzyskano odpowiedz od serwera %s.', response.url)
        for sel in response.xpath('//ul/li'):
            item = NikeItem()
            item['name'] = sel.xpath('normalize-space(a/text())').extract()
            item['link'] = sel.xpath('normalize-space(a/@href)').extract()
            item['description'] = sel.xpath('normalize-space(a/@data-subnav-label)').extract()
            yield item
"""
"""
def parse(self, response):
        self.logger.info('Uzyskano odpowiedz od serwera %s.', response.url)
        for sel in response.xpath('.//div//'):
            item = NikeItem()
            item['name'] = sel.xpath('normalize-space(a/text())').extract()
            item['link'] = sel.xpath('normalize-space(a/@href))').extract()
            item['description'] = sel.xpath('normalize-space(a/@href))').extract()
            yield item
"""


