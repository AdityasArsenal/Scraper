import scrapy

class BbbSpider(scrapy.Spider):
    name = "bbb"
    allowed_domains = ["www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328"]
    start_urls = ["https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"]

    def parse(self, response):
        products = response.css('div.sc-57fe1f38-0.eSrvHE')

        for product in products:
            yield{
                'name' : product.css('div.sc-95ea18ef-25.dOJDLL ::text').get(),
                'price' :  product.css('strong.amount ::text').get(),
                'sp' : product.css('div.sc-95ea18ef-24.gzboVs ::text').get(),
                'delivery' : product.css('div.sc-95ea18ef-34.gZsaNM b ::text').get(),
                'link' : 'https://www.noon.com/' + product.css('a').attrib['href'],
            }