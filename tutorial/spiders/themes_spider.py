import scrapy


class ThemesSpider(scrapy.Spider):
    name = "themes"
    start_urls = [
        'https://www.themes24x7.com/'
    ]

    def parse(self, response):
        for post in response.css('li.arya-blog-story-wrap a'):
            yield response.follow(post, callback=self.parse_post)

        # for a in response.css('div.pagination a'):
        #     yield response.follow(a, callback=self.parse)

    def parse_post(self, response):
        yield {
            'featured_image': response.css('div#arya-post-feat-img img::attr(src)').get(),
            'title': response.css('h1.arya-post-title::text').get(),
            'content': response.selector.xpath('/html/body/div[2]/div/div/div/article/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[1]').get(),
            'download_links': response.css('div.download-style p::text').getall(),
            'demo_link': response.css('a.demo::attr(href)').get(),
            'category': response.css('span.arya-post-cat::text').get(),
            'tags': response.css('div.arya-post-tags span a::text').getall(),
            'og:type': response.selector.xpath("//meta[@property='og:type']::attr(content)").get();
        }
