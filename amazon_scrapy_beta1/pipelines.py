# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class AmazonScrapyBeta1Pipeline:
    def process_item(self, item, spider):
        with open("search_result_items.txt", "+a") as f:
            f.write(json.dumps(dict(item)))
        return item
