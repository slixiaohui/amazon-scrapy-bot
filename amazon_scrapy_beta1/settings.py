# Scrapy settings for amazon_scrapy_beta1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "amazon_scrapy_beta1"
COOKIES = 'aws-target-data=%7B%22support%22%3A%221%22%7D; regStatus=registered; session-id=140-5847165-4522816; i18n-prefs=USD; ubid-main=135-8823416-4205865; x-main="cUc3XfetRayca@i9blFToyZUVtg7G3Tqj2G19OrC8MheBNykRqpUFYlzinD67ydg"; session-id-time=2082787201l; lc-main=en_US; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19834%7CMCMID%7C04734969658241011444510433180223385722%7CMCAAMLH-1714230319%7C9%7CMCAAMB-1714230319%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1713632719s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; aws-target-visitor-id=1705828858315-692221.45_0; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImRmMDYyMjgyLTE4OGUtNDdmYi1hNjc1LThiYjllYWNhMzc3NCJ9.eyJzdWIiOiIiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiaHR0cDpcL1wvc2lnbmluLmF3cy5hbWF6b24uY29tXC9zaWduaW4iLCJrZXliYXNlIjoiZEJKODREeXRITTNXNW5XaGd3SkNNR211RUNJVmNIck5jZlwvR3V0RVNTdkU9IiwiYXJuIjoiYXJuOmF3czppYW06Ojg0OTQ1ODE2MzY2ODpyb290IiwidXNlcm5hbWUiOiJuZW1vbWkzMjIwJTQwaXBwYWxzLmNvbSJ9.QLb0Hrr4xO1yvIjGCM_HYOb0hhHxlsVHCaNDa2WYcMuhpOGRs6ddjETN9Bv3HZiLDvYe-cXr7pJBlLGiXaiSrHlgCJGYTcy2XTI6NfkclpYoimtbXjRzm_EM2R3VBl1B; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Aiam%3A%3A849458163668%3Aroot%22%2C%22alias%22%3A%22%22%2C%22username%22%3A%22nemomi3220%2540ippals.com%22%2C%22keybase%22%3A%22dBJ84DytHM3W5nWhgwJCMGmuECIVcHrNcf%2FGutESSvE%5Cu003d%22%2C%22issuer%22%3A%22http%3A%2F%2Fsignin.aws.amazon.com%2Fsignin%22%2C%22signinType%22%3A%22PUBLIC%22%7D; session-token=U3IE5wvGt5kCpMd2cER34xXF9hTttOjqW7qMpOuZDWvzm7AZbD81WVxNgWLYqR2C6lWpduacvlAblqqbf8MjAe3Stoi/aFsnFft1X9j519QV2jbtlXSXUcuACDUs0COtU33H5X4j+db4PQGIrl8dA7X8UmNKuZH1WPAftDOhYr6apCQ9gJoAz7m9PSaWka7hvjnqYb5Q0jX/d6ka3YFUBNr7QHfWb+RkRyCCe8Sy2M9j7+yzNFhfsMus9lFkKClBrt9bzMLmLLtr/Qx6QNCM190nOotUl36D38gngYhoxVga3i87u2t+cefIJBjMvfriL/fjn99hfg3hqfFk33snNZq3hqJQ6Da8oVMFd0Xcmpdve+ywkMLDII7GYFk68xHN; s_cc=true; s_vnum=2145791600879%26vn%3D1; s_invisit=true; s_dslv_s=First%20Visit; s_c27=GLSBYFE9MGKKQXXM; s_sq=%5B%5BB%5D%5D; s_ppv=86; s_nr=1713791634826-New; s_dslv=1713791634828; csm-hit=tb:X4CVPZ8WFWNH4F3H7CCT+s-B0W7EBT0VXYR5E2GPZ6G|1713791693805&t:1713791693805&adb:adblk_yes'

SPIDER_MODULES = ["amazon_scrapy_beta1.spiders"]
NEWSPIDER_MODULE = "amazon_scrapy_beta1.spiders"

ROBOTSTXT_OBEY = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "amazon_scrapy_beta1 (+http://www.yourdomain.com)"
## settings.py

# USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "amazon_scrapy_beta1.middlewares.AmazonScrapyBeta1SpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "amazon_scrapy_beta1.middlewares.AmazonScrapyBeta1DownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "amazon_scrapy_beta1.pipelines.AmazonScrapyBeta1Pipeline": 300,
    "amazon_scrapy_beta1.pipelines.PostgreSQLPipeline": 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
## settings.py
DOWNLOAD_DELAY = 5
LOG_LEVEL = "INFO"

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    "amazon_scrapy_beta1.middlewares.RetryMiddleware": 550,
    "scrapy_fake_useragent.middleware.RandomUserAgentMiddleware": 400,
    "scrapy_fake_useragent.middleware.RetryUserAgentMiddleware": 401,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 1,
}


DATABASE_SETTINGS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "ts123456",
    "host": "localhost",
    "port": "5432",
}


# 配置代理服务器地址和端口
HTTP_PROXY = "http://127.0.0.1:8080"

FAKEUSERAGENT_PROVIDERS = [
    "scrapy_fake_useragent.providers.FakeUserAgentProvider",  # This is the first provider we'll try
    "scrapy_fake_useragent.providers.FakerProvider",  # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    "scrapy_fake_useragent.providers.FixedUserAgentProvider",  # Fall back to USER_AGENT value
]


# jdbc:postgresql://localhost:5432/postgres
