import scrapy

class ganjoorExtractor(scrapy.Spider):
    name = 'ganjoor'
    custom_settings = {
        'CONCURRENT_REQUESTS': 64,
        'DOWNLOAD_DELAY': 0,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 64,
        'ITEM_PIPELINES':{
            'tutorial.pipelines.ganjoor.ganjoorPipeline': 300,
        }
    }
    ### IMPORTANT
    # Enter the absolute path that you want output's to save
    output_dir = '' #example: '/home/mrt/Desktop/personal/scrapy/tutorial/tutorial/data'
    allowed_domains = ['ganjoor.net']
    def start_requests(self):
        url = 'https://ganjoor.net/'

        yield scrapy.Request(url, callback=self.poet_extractor, dont_filter=True)

    def poet_extractor(self, response):
        poets = response.xpath('//div[@class="poet"]/a/@href').extract()
        poets = list(set(poets))
        
        for poet in poets:
            author = poet.split('/')[-2]
            yield scrapy.Request(url=poet, callback=self.poem_extractor,
                                 dont_filter=True, meta={'author': author})

    def poem_extractor(self, response):
        urls = response.xpath('//a/@href').extract()
        author = response.meta['author']
        poems = []
        for link in urls:
            if response.url in link and link not in poems:
                poems.append(link)

        poems = list(set(poems))
        for poem in poems:
            yield scrapy.Request(url=poem, callback=self.final_extraction,
                                  dont_filter=False, meta={'author': author})

    def final_extraction(self, response):
        poems = response.xpath('//div[@class="m1"]/p/text()').extract()
        author = response.meta['author']
        if not poems:
            yield scrapy.Request(url=response.url, callback=self.poem_extractor,
                                 dont_filter=True, meta={'author': author})
        else:
            final = ''

            m1 = response.xpath('//div[@class="m1"]/p/text()').extract()
            m2 = response.xpath('//div[@class="m2"]/p/text()').extract()
            
            for i in range(0,len(m1)):
                final += m1[i]+'\n'+m2[i]+'\n'  
        
            yield {
                'author': author,
                'poem': final,
                'output_dir': self.output_dir
            }
