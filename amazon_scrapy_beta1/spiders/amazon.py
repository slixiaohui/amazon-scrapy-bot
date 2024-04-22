import scrapy
from scrapy import Request
from amazon_scrapy_beta1.items import ProductItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    q = "roborock"
    base_url = "https://www.amazon.com"
    start_urls = [f"https://www.amazon.com/s?k={q}"]
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "Upgrade-Insecure-Requests": 1,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.amazon.com/s?k=roborock",
    }

    def start_requests(self):
        yield Request(
            url=self.start_urls[0],
            headers=self.headers,
            callback=self.parse,
            meta={"keyword": self.q, "page": 1},
        )

    def parse(self, response):
        products = response.css(
            "div.s-result-item[data-component-type=s-search-result]"
        )
        next_page = response.css(
            "a.s-pagination-next::attr(href)"
        ).get()  # search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(33) > div > div > span > a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator
        if next_page:
            next_url = self.base_url + next_page
            yield Request(
                url=next_url,
                headers=self.headers,
                callback=self.parse,
                # meta={"keyword": self.q, "page": 1},
            )

        for product in products:
            relative_url = product.css("h2 a::attr(href)").get()
            product_detail_url = self.base_url + relative_url

            item = ProductItem()
            name = product.css("h2>a>span::text").get()
            price = product.css("span.a-offscreen::text").get()
            no_of_ratings = product.css(
                "div.a-section.a-spacing-none.a-spacing-top-micro>div>span::attr(aria-label)"
            ).get()
            offers = product.css(".a-badge-text::text").get()
            item["name"] = name
            item["price"] = price
            item["no_of_ratings"] = no_of_ratings
            item["offers"] = offers
            yield item

            yield scrapy.Request(
                url=product_detail_url,
                callback=self.parse_product_detail,
                headers=self.headers,
                # meta={"keyword": self.q, "page": 1},
            )

    def parse_product_detail(self, response):
        # print(response.text)
        pass
