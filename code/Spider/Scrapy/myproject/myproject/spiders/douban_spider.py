import scrapy

class DoubanSpiderSpider(scrapy.Spider):
    # 定义爬虫名称（必须唯一）
    name = "douban_spider"  

    # 限制爬虫的访问域名，防止爬取其他域名的网页
    allowed_domains = ["movie.douban.com"]  
    
    # 定义爬虫的起始页面，爬虫将从这些页面开始抓取
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://movie.douban.com/',
        }
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)
    
    # parse方法，每个爬虫的核心，用于处理相应并提取数据。
    # 它接收一个response对象，表示服务器返回的页面内容
    def parse(self, response):
        for movie in response.css('div.item'):
            yield {
                'title': movie.css('span.title::text').get(),
                'rating': movie.css('span.rating_num::text').get(),
                'quote': movie.css('span.inq::text').get(),
            }

        # 处理分页
        next_page = response.css('span.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
