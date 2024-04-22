# amazon-scrapy-bot
一个爬取亚马逊商品的爬虫，基于scrapy

## 结果样例
1. 查询关键词得出的首页html在`search_result.txt`
2. 根据首页爬取的商品信息在`search_result_items.txt`

## 待完善
- [ ] 反爬虫机制
amazon对爬虫的控制似乎十分严格，爬取频率、user-agent似乎都有影响，目前采取的是加了个中间件`RetryMiddleware`暴力重试，后面用代理ip，再结合别的大佬的代码看看怎么搞
- [ ] 爬取sku商品明细
