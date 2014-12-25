#!/usr/bin/python
# -*-coding:utf-8-*-
"""Scrapy Middleware to set a random User-Agent for every Request.

Downloader Middleware which uses a file containing a list of
user-agents and sets a random one for each request.
"""

import random
from scrapy import signals
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

__author__ = "Srinivasan Rangarajan"
__copyright__ = "Copyright 2014, Srinivasan Rangarajan"
__credits__ = ["Srinivasan Rangarajan"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Srinivasan Rangarajan"
__email__ = "srinivasanr@gmail.com"
__status__ = "Development"


class RandomUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, settings, user_agent='Scrapy'):
        super(RandomUserAgentMiddleware, self).__init__()
        self.user_agent = user_agent
        user_agent_list_file = settings.get('USER_AGENT_LIST')
        with open(user_agent_list_file, 'r') as f:
            self.user_agent_list = [line.strip() for line in f.readlines()]

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls(crawler.settings)
        crawler.signals.connect(obj.spider_opened,
                                signal=signals.spider_opened)
        return obj

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent_list)
        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
