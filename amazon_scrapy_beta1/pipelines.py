# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import psycopg2
import psycopg2


class PostgreSQLPipeline:
    def __init__(self, db_settings):
        self.db_settings = db_settings

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DATABASE_SETTINGS")
        return cls(db_settings)

    def open_spider(self, spider):
        self.conn = psycopg2.connect(**self.db_settings)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            # 将 item 写入 PostgreSQL 数据库中的表
            insert_query = """
            INSERT INTO amazon.products (asin, name, price, no_of_ratings, n_ratings, offers,product_detail_url, price_unit)
            VALUES (%s, %s, %s, %s,%s, %s, %s, '$')
            """
            item_data = (
                item["asin"],
                item["name"],
                item["price"],
                item["no_of_ratings"],
                item["n_ratings"],
                item["offers"],
                item["product_detail_url"],
            )
            self.cur.execute(insert_query, item_data)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            spider.logger.error(f"Error processing item: {e}")
        return item


class AmazonScrapyBeta1Pipeline:
    def process_item(self, item, spider):
        with open("search_result_items.txt", "+a") as f:
            f.write(json.dumps(dict(item)))
        return item
