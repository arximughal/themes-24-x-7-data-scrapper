import scrapy


class ThemesSpider(scrapy.Spider):
    name = "themes"
    start_urls = [
        'https://www.themes24x7.com/'
    ]

    def parse(self, response):
        # post_links = response.css('li.arya-blog-story-wrap a')
        # yield from response.follow_all(post_links, self.parse_post)
        for post in response.css('li.arya-blog-story-wrap a'):
            yield response.follow(post, callback=self.parse_post)
        
        # for quote in response.css('li.arya-blog-story-wrap'):
        #     post_link = response.css('li.arya-blog-story-wrap a::attr(href)')
        #     response.follow(post_link)
        #     yield response.follow()
        #     yield {
        #         'title': quote.css('div.arya-blog-story-text h2::text').get(),
        #         'category': quote.css('span.arya-cd-cat::text').get(),
        #         'image': quote.css('div.arya-blog-story-img img::attr(src)').getall()
        #     }
        
        for a in response.css('div.pagination a'):
            yield response.follow(a, callback=self.parse)

    def parse_post(self, response):
        # def extract_with_css(query):
        #     return response.css(query).get(default='').strip()

        yield {
            'featured_image': response.css('div#arya-post-feat-img img::attr(src)').get(),
            'title': response.css('h1.arya-post-title::text').get(),
            'content': response.selector.xpath('/html/body/div[2]/div/div/div/article/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/p[1]').get(),
            'download_links': response.css('div.download-style p::text').getall(),
            'demo_link': response.css('a.demo::attr(href)').get()
        }