# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector

from Nike.items import NikeItem
from Nike.items import obiekt

#klasa definiujaca spidera i jego zachowanie
class NikeSpider(scrapy.Spider):
    name = "NikeSpider"
    allowed_domains = ["store.nike.com/gb/en_gb/pw/mens-shoes/7puZoi3"]
    start_urls = [
        "http://store.nike.com/gb/en_gb/pw/mens-shoes/7puZoi3"
    ]
#w przypadku poprawnej odpowiedzi wypisanie w logu jego adresu
#extract określonych danych(nazwa,cena)
    def parse(self, response):
        self.logger.info('Uzyskano odpowiedz od serwera %s.', response.url)
        produkty = Selector(response).xpath('//div[@id="body"')
        for produkt in produkty:
            item = obiekt()
            item['name'] = produkt.xpath('normalize-space(a[@class = "product-name/text())').extract()[0]
            item['price'] = produkt.xpath('normalize-space(a[@class = "prices/text())').extract()[0]
            yield item
#w przypadku poprawnej odpowiedzi wypisanie w logu jego adresu
#extract określonych danych(nazwa,link,opis) -- działa w przypadku alloweddomains i start urls store.nike.com/gb/en_gb
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



