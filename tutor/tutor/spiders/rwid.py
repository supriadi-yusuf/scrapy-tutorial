import scrapy
from scrapy.http.response.html import HtmlResponse


class RwidSpider(scrapy.Spider):
    name = "rwid"
    allowed_domains = [""]
    start_urls = ["http://jobstreet.co.id"]

    def parse(self, response: HtmlResponse):
        data = {
            'emailAddress_seekanz': 'superriyadi@yahoo.com',
            'password_seekanz': '190277SupriAdi',

        }

        print('tipe data : ', type(response))
