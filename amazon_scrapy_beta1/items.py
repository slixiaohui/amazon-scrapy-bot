# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScrapyBeta1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductItem(scrapy.Item):
    asin = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    no_of_ratings = scrapy.Field()
    n_ratings = scrapy.Field()
    offers = scrapy.Field()
    product_detail_url = scrapy.Field()
