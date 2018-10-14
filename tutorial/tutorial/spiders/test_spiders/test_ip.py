# -*- coding: utf-8 -*-
import scrapy
from time import sleep

class TestSpider(scrapy.Spider):
    name = 'test_ip'
    custom_settings = {
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 0,
        # 'DOWNLOADER_MIDDLEWARES': {
           # 'tutorial.middlewares.middlewares.TutorialDownloaderMiddleware': 543,
           # 'tutorial.middlewares.Tor.TorMiddleware': 100,   
        # }
    }
    def start_requests(self):
        url = 'http://checkip.amazonaws.com'
        while True:
            yield scrapy.Request(url, dont_filter=True, callback=self.parse)
            sleep(0.5)

    def parse(self, response):

        yield {
            'your ip': response.text
        }