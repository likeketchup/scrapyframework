# -*- coding:utf-8 -*-
import scrapy
import re
from mysql import MySQL
import datetime
from scrapy.http import Request
from QQspider.items import QqspiderItem


def find_domain(url):
    domain = re.findall(r'http://[\w.]*.qq.com/', url)[0]
    return domain


def judge_url(url):
    if re.match(r'http://\w*', url):
        return 1
    return 0


def insert_data(data):
	n=MySQL()
	sql = "select id from urls_crawled where url='"+data['url']+"';"
	result = n.query(sql)
	if result == 0:
		try:
			n.insert('urls_crawled',data)
		except:
			return 200
	n.commit()


def get_data(url,time,date):
    data = {}
    data["domain"] = ''
    data["url"] = url
    data['time'] = time
    data['date'] = date


class QQSpider(scrapy.Spider):
    name = "qq_main"
    allowed_domains = ["qq.com"]
    start_urls = [
        "http://www.qq.com/"
    ]

    def parse(self, response):
        if response.status == 200:
            db = MySQL
            db.insert("urls_crawled", response.url)
            db.commit()
            urls = set()
            for sel in response.xpath('//a'):
                url_link = sel.xpath("@href").extract()
                if judge_url(url_link):
                    url_link = url_link[0].encode("utf-8")
                    url_link.get_data()

