# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class NikePipeline(object):
    def process_item(self, item, spider):
        return item
    """
class NikePipelineCena(object):
    def process_item(self, item, spider):
        if item['price'] < 100

        return item
"""