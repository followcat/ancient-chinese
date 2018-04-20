# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from acscrapy.items import AcscrapyItem


class A911chengyuSpider(scrapy.Spider):
    name = '911chengyu'

    allowed_domains = ['chengyu.911cha.com']
    start_urls = ['http://chengyu.911cha.com/']

    item_keys_map = {
        '成语解释': 'explain',
        '成语出处': 'origin',
        '成语繁体': 'traditional',
        '成语简拼': 'jianpin',
        '成语注音': 'phonetic',
        '常用程度': 'level',
        '成语字数': 'number',
        '感情色彩': 'emotional',
        '成语用法': 'usage',
        '成语结构': 'structure',
        '成语年代': 'years',
        '成语例子': 'example',
        '英语翻译': 'english',
        '俄语翻译': 'russian',
        '其他翻译': 'otherese',
        '成语谜语': 'riddle',
        '成语故事': 'story',
        '成语正音': 'pronunciation',
        '成语辨形': 'recognition',
        '近义词': 'similar',
        '反义词': 'antonym',
        '日语翻译': 'japanese'
    }

    def parse(self, response):
        links = response.selector.xpath('//a')
        for link in links:
            new_url = link.xpath('@href').extract()[0]
            if new_url.startswith('./pinyin_'):
                yield Request('http://chengyu.911cha.com/'+new_url,
                              callback=self.PinyinParse)

    def PinyinParse(self, response):
        links = response.selector.xpath('//*[contains(@class, "l5 center f14")]//li//a')
        for link in links:
            new_url = link.xpath('@href').extract()[0]
            yield Request('http://chengyu.911cha.com/'+new_url,
                          callback=self.WordParse)

    def WordParse(self, response):
        item = AcscrapyItem()
        item['url'] = response.url
        item['title'] = response.xpath(
            '//*[contains(@class, "leftbox")]//*[contains(@class, "panel")]//*[contains(@class, "mcon")][1]//h2//text()')[0].extract()
        item['pinyin'] = response.xpath(
            '//*[contains(@class, "gray mt f16")]//text()')[0].extract()
        for data in response.xpath(
                  '//*[contains(@class, "mcon bt noi f14")]//p'):
            text = data.xpath('string(.)').extract()[0]
            for key, value in self.item_keys_map.items():
                if text.startswith(key):
                    text = text.replace(key, '').replace('911cha.com', '')
                    item[value] = text
        return item
