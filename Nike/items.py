# -*- coding: utf-8 -*-



import scrapy

#budowa modelu danych pobieranych ze strony
#(nazwa,link,opis)
class NikeLink(scrapy.Item):
    link = scrapy.Field()
#sprawdz wszystkie przedmioty na stanie
class obiekt(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
class NikeShoe(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()