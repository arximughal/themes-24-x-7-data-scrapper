import scrapy


class ThemesSpider(scrapy.Spider):
    name = "themes"
    start_urls = [
        'https://www.themes24x7.com/'
    ]

    def parse(self, response):
        for post in response.css('li.arya-blog-story-wrap a'):
            yield response.follow(post, callback=self.parse_post)

        for a in response.css('div.pagination a'):
            yield response.follow(a, callback=self.parse)

    def parse_post(self, response):
        yield {
            'featured_image': response.css('div#arya-post-feat-img img::attr(src)').get().replace('themes24x7', 'CestaFina'),
            'title': response.css('h1.arya-post-title::text').get().replace('themes24x7', 'CestaFina'),
            'content': response.selector.xpath('/html/body/div[2]/div/div/div/article/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[1]').get().replace('themes24x7', 'CestaFina'),
            'download_links': response.css('div.download-style p::text').getall(),
            'demo_link': response.css('a.demo::attr(href)').get(),
            'category': response.css('span.arya-post-cat::text').get().replace('themes24x7', 'CestaFina'),
            'tags': response.css('div.arya-post-tags span a::text').getall(),
            'og:type': response.selector.xpath("//meta[@property='og:type']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:image': response.selector.xpath("//meta[@property='og:image']/@content")[0].extract(),
            'twitter:image': response.selector.xpath("//meta[@name='twitter:image']/@content")[0].extract(),
            'og:url': response.selector.xpath("//meta[@property='og:url']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:title': response.selector.xpath("//meta[@property='og:title']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:locale': response.selector.xpath("//meta[@property='og:locale']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:type': response.selector.xpath("//meta[@property='og:type']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:description': response.selector.xpath("//meta[@property='og:description']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:image': response.selector.xpath("//meta[@property='og:image']/@content")[0].extract(),
            'og:image:secure_url': response.selector.xpath("//meta[@property='og:image:secure_url']/@content")[0].extract(),
            'og:image:width': response.selector.xpath("//meta[@property='og:image:width']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'og:image:height': response.selector.xpath("//meta[@property='og:image:height']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'twitter:card': response.selector.xpath("//meta[@name='twitter:card']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'twitter:url': response.selector.xpath("//meta[@name='twitter:url']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'twitter:title': response.selector.xpath("//meta[@name='twitter:title']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'twitter:description': response.selector.xpath("//meta[@name='twitter:description']/@content")[0].extract().replace('themes24x7', 'CestaFina'),
            'twitter:image': response.selector.xpath("//meta[@name='twitter:image']/@content")[0].extract()
        }
