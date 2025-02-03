import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for link in response.css('#index-by-category a[href^=\'pep\']'):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            'h1.page-title::text').re(r'^PEP\D*(?P<number>\d+)\W*(?P<name>.+)')
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css(
                'dt:contains(\'Status\') + dd > abbr::text').get()
        )
