# -*- coding: utf-8 -*-
import scrapy
from time import sleep

class TestSpider(scrapy.Spider):
	name = 'test_ip'

	def start_requests(self):
		url = 'http://checkip.amazonaws.com'
		while True:
			yield scrapy.Request(url, dont_filter=True, callback=self.parse)
			sleep(0.5)

	def parse(self, response):

		yield {
			'your ip': response.text
		}