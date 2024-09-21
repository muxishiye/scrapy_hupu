# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class MongoPipeline:
    def open_spider(self,spider):
        # 获取mongo链接
        self.client = pymongo.MongoClient()
        # 指定具体的数据库
        self.hupu = self.client.hupu.article

    def process_item(self, item, spider):
        self.hupu.insert_one(item)
        return item

    def close_spider(self,spider):
        self.client.close()