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

        # Follow pagination links and scrape next pages
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
