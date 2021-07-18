from .base_spider import BaseSpider


class TikiSpider(BaseSpider):
    name = "tiki.vn"

    def parse(self, response):
        item = response.meta.get('item', {})
        item['url'] = response.url
        item['title'] = response.css("span#productTitle::text").extract_first("").strip()
        item['price'] = float(
            response.css("span#product-price__current-price::text").re_first("\$(.*)") or 0
        )
        yield item
