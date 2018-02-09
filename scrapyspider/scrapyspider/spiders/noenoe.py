import scrapy
import os
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):
    name = "noenoe"

    def start_requests(self):
        urls = ['http://noenoe4126.blog9.fc2.com/page-' + str(i) + '.html'
                for i in range(0,150)] 
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        imgs = response.xpath('//a[contains(@href,"blog-imgs-") and contains(@href,"noenoe4126") and contains(@href,".jpg")]/@href').extract()
        for img in imgs:
            yield scrapy.Request(url=img, callback=self.parseImg)
            
            #name = img.url.split("/")[-1]
            #with open(name, 'wb') as f:
            #    f.write()
        #name = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)

    def parseImg(self, response):
        fileName = response.url.split("/")[-1]
        filePath = '/home/dd2645/noenoeOut/' + fileName
        if os.path.exists(filePath) == False :
            with open(filePath, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % fileName)
