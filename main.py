import scrapy

class NoonSpider(scrapy.Spider):
    name = 'noon_spider'
    start_urls = ['https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/']

    def parse(self, response):
        # Iterate over each product container on the page
        products = response.css('div.sc-b1fef3a-10 bFBwRJ grid')  # Example class, adjust according to the actual HTML

        for product in products:
            yield {
                'name': product.css('div.sc-33a5583c-25 eQerwk::text').get()
            }

spy = NoonSpider()

sponserd_class = 'div.sc-95ea18ef-24.gzboVs'

cclass="sc-33a5583c-23.hoKgLx"