# -*- coding: utf-8 -*-

# Define your item pipelines here
from scrapy.exceptions import DropItem

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AllegroPipeline(object):
    def process_item(self, item, spider):
        return item


class PricePipeline(object):

    def process_item(self, item, spider):

        # to test if only "job_id" is empty,
        # change to:
        # if not(item["job_id"]):
        if not(all(item.values())):
            raise DropItem()
        else:
            return item