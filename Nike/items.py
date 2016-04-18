# -*- coding: utf-8 -*-



import scrapy

#budowa modelu danych pobieranych ze strony
#(nazwa,link,opis)
class NikeItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
#sprawdz wszystkie przedmioty na stanie
class obiekt(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()