# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    pinyin = scrapy.Field()
    explain = scrapy.Field()
    origin = scrapy.Field()
    traditional = scrapy.Field()
    jianpin = scrapy.Field()
    phonetic = scrapy.Field()
    level = scrapy.Field()
    number = scrapy.Field()
    emotional = scrapy.Field()
    usage = scrapy.Field()
    structure = scrapy.Field()
    years = scrapy.Field()
    example = scrapy.Field()
    english = scrapy.Field()
    russian = scrapy.Field()
    otherese = scrapy.Field()
    riddle = scrapy.Field()
    story = scrapy.Field()
    pronunciation = scrapy.Field()
    recognition = scrapy.Field()
    similar = scrapy.Field()
    antonym = scrapy.Field()
    japanese = scrapy.Field()
