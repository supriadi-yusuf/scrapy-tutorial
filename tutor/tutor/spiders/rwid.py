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

        return scrapy.FormRequest(
            url='/login',
            formdata=data,
            callback=self.after_login
        )

    def after_login(self, response):
        # ambil semua items
        detail_products = response.css('.card .card-title a')
        for detail in detail_products:
            href = detail.attrib('href')
            yield response.follow(href, callback=self.parse_detail)

        # ambil pagination
        paginations: List[Selector] = response.css('.pagination a.page-link')
        for pagination in paginations:
            href = pagination.attrib.get('href')
            yield response.follow(href, callback=self.after_login)

    def parse_detail(self, response):
        image = response.css('.card-img-top').get()
        title = response.css('.card-title::text').get()
        stock = response.css('.card-stock::text').get()
        description = response.css(".card-text::text").get()

        return {
            'image': image,
            'title': title,
            'stock': stock,
            'description': description,
        }
