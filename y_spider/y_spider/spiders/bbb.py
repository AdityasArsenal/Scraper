import scrapy
import random

class BbbSpider(scrapy.Spider):
    name = "bbb"
    allowed_domains = ["www.noon.com"]
    start_urls = ["https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"]

# for some resone this is way more time consuming
    #user_agents = [
    #'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0', 
    #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 
    #'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    #'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',]
    

    i = 0
    links = []
    prices = []

    def parse(self, response):
        products = response.css('div.sc-57fe1f38-0.eSrvHE')

        for product in products:
            BbbSpider.i += 1
            self.links.append('https://www.noon.com' + product.css('a ::attr(href)').get())
            self.prices.append(product.css('strong.amount ::text').get())

            full_name = product.css('div.sc-95ea18ef-25.dOJDLL ::text').get()
            brand = full_name.split()[0]

            if product.css('div.sc-95ea18ef-24.gzboVs ::text').get() ==  'Sponsored':
                yield{
                    'Rank' : BbbSpider.i,
                    'brand' : brand,
                    'Name' : full_name,
                    'Price' :  product.css('strong.amount ::text').get(),
                    'Sponsored' : 'Y',
                    'Delivery by' : product.css('div.sc-95ea18ef-34.gZsaNM b ::text').get(),
                    'Link' : 'https://www.noon.com' + product.css('a ::attr(href)').get(),
                    'Delivery type' :  product.css('div.sc-d376b94d-3.dFzhiL img ::attr(alt)').get(),
                    'Sale' :  product.css('div.sc-824ecd5d-0.ynPBp ::text').get(),
                    'Rating' :  product.css('div.sc-9cb63f72-2.dGLdNc ::text').get(),
                    'Total reviews' :  product.css('div.sc-9cb63f72-4.gBbbhg span ::text').get(),
                    'Offers' : product.css('span.discount ::text').get()
                }

            else:
                yield{
                    'Rank' : BbbSpider.i,
                    'brand' : brand,
                    'Name' : full_name,
                    'Price' :  product.css('strong.amount ::text').get(),
                    'Sponsored' : 'N',
                    'Delivery by' : product.css('div.sc-95ea18ef-34.gZsaNM b ::text').get(),
                    'Link' : 'https://www.noon.com' + product.css('a ::attr(href)').get(),
                    'Delivery type' :  product.css('div.sc-d376b94d-3.dFzhiL img ::attr(alt)').get(),
                    'Sale' :  product.css('div.sc-824ecd5d-0.ynPBp ::text').get(),
                    'Rating' :  product.css('div.sc-9cb63f72-2.dGLdNc ::text').get(),
                    'Total reviews' :  product.css('div.sc-9cb63f72-4.gBbbhg span ::text').get(),
                    'Offers' : product.css('span.discount ::text').get()
                }

        next_pages = [
            'https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?isCarouselView=false&limit=50&page=2&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc',
            'https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?isCarouselView=false&limit=50&page=3&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc',
            'https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/?isCarouselView=false&limit=50&page=4&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc'
        ]

        for next_page in next_pages:                                
            yield response.follow(next_page, callback= self.parse)
            # headers = {'User-Agent': random.choice.(user_agent)}
            # this is a slow the spider

