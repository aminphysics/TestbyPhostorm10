# -*- coding: utf-8 -*-
import scrapy

class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']
def parse(self, response):
    quotes = response.css(".score.unvoted::text").extract()
    yield {'quotes': quotes}
