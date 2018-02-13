import scrapy
import os
from scrapy.selector import Selector
from urllib.parse import urljoin

class QuotesSpider(scrapy.Spider):
    name = "willothewisp"

    def start_requests(self):
        urls = ['http://h5n.jp/willothewisp/w_moon_vs_villa/index.html',
                'http://h5n.jp/willothewisp/w_moon_vs_villa/moon_vs_villa_02.html',
                'http://h5n.jp/willothewisp/w_moon_vs_villa/moon_vs_villa_03.html',
                'http://h5n.jp/willothewisp/w_moon_story1/index.html'] + \
                ['http://h5n.jp/willothewisp/w_moon_story1/moon_story1_' + 
                        '{:0>2d}'.format(i) + '.html' for i in range(2,6)] + \
                ['http://h5n.jp/willothewisp/w_moon_story2/index.html',
                'http://h5n.jp/willothewisp/w_moon_story2/moon_story2_02.html',
                'http://h5n.jp/willothewisp/w_moon_story2/moon_story2_03.html',
                'http://h5n.jp/willothewisp/w_moon_story3/index.html'] + \
                ['http://h5n.jp/willothewisp/w_moon_story3/moon_story3_' + 
                        '{:0>2d}'.format(i) + '.html' for i in range(2,16)] + \
                ['http://h5n.jp/willothewisp/w_moon_story4/index.html'] + \
                ['http://h5n.jp/willothewisp/w_moon_story4/moon_story4_' + 
                        '{:0>2d}'.format(i) + '.html' for i in range(2,10)] + \
                ['http://h5n.jp/willothewisp/w_moon_story5/index.html'] + \
                ['http://h5n.jp/willothewisp/w_moon_story5/moon_story5_' +
                        '{:0>2d}'.format(i) + '.html' for i in range(2,13)] + \
                ['http://h5n.jp/willothewisp/w_moon_ex_sp_a/index.html'] + \
                ['http://h5n.jp/willothewisp/w_moon_ex_sp_a/moon_ex_sp_a_' +
                        '{:0>2d}'.format(i) + '.html' for i in range(2,18)] + \
                ['http://h5n.jp/willothewisp/w_goddess_singleimage/index.html'] + \
                ['http://h5n.jp/willothewisp/w_goddess_singleimage/singleimage_' + 
                        '{:0>2d}'.format(i) + '.html' for i in range(2,6)]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        imgs = response.xpath('//a[contains(@href,".jpg")]/@href').extract()
        fullPath = [urljoin(response.url, item.strip()) for item in imgs]
        for img in fullPath:
            yield scrapy.Request(url=img, callback=self.parseImg)
    
    def parseImg(self, response):
        fileName = response.url.split("/")[-1]
        filePath = '/home/dd2645/willothewisp/' + fileName
        if os.path.exists(filePath) == False :
            with open(filePath, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % fileName)
