# amazon-scrapy-bot
一个爬取亚马逊商品的爬虫，基于scrapy

## 结果样例
商品项包含：
- asin
- 商品名称
- 价格
- 价格单位（$）
- 评分
- reviews数量
- 促销活动
- 商详页链接
1. 通过`PostgreSQLPipeline`将商品项写入到了PostgreSQL中，数据库中的数据如下
<img width="1384" alt="image" src="https://github.com/slixiaohui/amazon-scrapy-bot/assets/81063796/2cc0f7db-b2ce-4d58-8d6e-4befdd09ff27">

2. 查询关键词得出的首页html在`search_result.txt`
3. 根据首页爬取的商品信息在`search_result_items.txt`

## 待完善
- [ ] 反爬虫机制
amazon对爬虫的控制似乎十分严格，爬取频率、user-agent似乎都有影响，目前采取的是加了个中间件`RetryMiddleware`暴力重试，后面用代理ip，再结合别的大佬的代码看看怎么搞
- [ ] 爬取sku商品明细
## 数据分析
- [ ] BI分析
    - [ ] 标题关键词分析->广告投放和listing优化
    - [ ] niche商品分析->长尾商品挖掘
