import scrapy

class BbbSpider(scrapy.Spider):
    name = "bbb"
    allowed_domains = ["www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328"]
    start_urls = ["https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"]

    def parse(self, response):
        products = response.css('div.sc-57fe1f38-0.eSrvHE')
        print(len(products))

        i = 0
        for product in products:
            i += 1
            yield{
                'Rank' : i,
                'name' : product.css('div.sc-95ea18ef-25.dOJDLL ::text').get(),
                'price' :  product.css('strong.amount ::text').get(),
                'sp' : product.css('div.sc-95ea18ef-24.gzboVs ::text').get(),
                'delivery by' : product.css('div.sc-95ea18ef-34.gZsaNM b ::text').get(),
                'link' : 'https://www.noon.com//' + product.css('a').attrib['href'],
                'exp' :  product.css('div.sc-d376b94d-3.dFzhiL img').attrib['alt'].replace('noon-',''),
                'sale' :  product.css('div.sc-824ecd5d-0.ynPBp ::text').get(),
                'rating' :  product.css('div.sc-9cb63f72-2.dGLdNc ::text').get(),
                'Total reviews' :  product.css('div.sc-9cb63f72-4.gBbbhg span ::text').get()
            }