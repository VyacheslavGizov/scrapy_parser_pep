import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсит ссылки на документы PEP."""

        rows = response.css('#index-by-category tbody tr')
        for row in rows:
            yield response.follow(
                row.css('a::attr(href)').get(),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Парсит страницы документов."""

        number, name = response.css(
            'h1.page-title::text').re(r'^PEP\D*(?P<number>\d+)\W*(?P<name>.+)')
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css(
                'dt:contains(\'Status\') + dd > abbr::text').get()
        )
