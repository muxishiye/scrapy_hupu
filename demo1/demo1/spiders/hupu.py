import time
import scrapy

class HupuSpider(scrapy.Spider):
    name = "hupu"
    allowed_domains = ["www.hupu.com",'bbs.hupu.com']
    page = 1
    start_urls = [f"https://www.hupu.com/home/v1/news?pageNo={page}&pageSize=100"]

    def parse(self, response):
        """
        该函数用于获取详情页链接
        """
        # 获取json数据页的data值
        datas = response.json()['data']
        # 设置cookie
        cookie = {
            'smidV2': '20240621154411a48ec0a3ab9321b62a5f41a481f530e100f3789646777c680',
            '_HUPUSSOID': '395f8017-7075-444c-8ba3-45d792093921',
            'tfstk': 'fGArNvjrfbhzw4vh0i1Fbi5t055R91n6tBsC-eYhPgjlOYIhxeKARWTHOWYH5iO5VU1uKtjDmgtWFes20_dXFWsS268Hf6osffG6yUCAtcisVGdIk1bzE8qCxiX0lstBsfG6yU45rVTm12nLmEjFx6XlKtXcDNqht9XouibFWJqkx602oiQF-ujhtZfc5NynZ9Tk-S71EV4TuHF_fFXPjEkTtWPlulswr0Vg_IJVUGVF0WVHga8vLdKU_vsMBg61fncba68c83sXjfVViOJ9Rw-ra7fWnKdRNIiaWT-FVOAf3A42b_-FIQX4-WTPTiCVoC0QBiOVVHAPnVNNdsA1I_vjH06CaN-Hw3zUthYX5QBvTcrcvL_OiNT-aS5MrwjPxkQ0kYRpUk2FEZQVfqumc8KhYNLUlIyLptfOuGg5PJedEZQVfqu4pJBcDZSsPa1..',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22190adfd2ac02126-07d5046cb892a58-4c657b58-2073600-190adfd2ac119de%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwYWRmZDJhYzAyMTI2LTA3ZDUwNDZjYjg5MmE1OC00YzY1N2I1OC0yMDczNjAwLTE5MGFkZmQyYWMxMTlkZSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22190adfd2ac02126-07d5046cb892a58-4c657b58-2073600-190adfd2ac119de%22%7D',
            'Hm_lvt_4fac77ceccb0cd4ad5ef1be46d740615': '1720906204',
            'Hm_lvt_b241fb65ecc2ccf4e7e3b9601c7a50de': '1720906204',
            'csrfToken': 'ngKipZkzUJKFFl78XarHoW4o',
            'Hm_lvt_df703c1d2273cc30ba452b4c15b16a0d': '1726920698',
            'HMACCOUNT': '3BCD12C23A0CF7EC',
            'Hm_lpvt_df703c1d2273cc30ba452b4c15b16a0d': '1726920705',
            'acw_tc': 'ac11000117269255497467561e0133b3da95bd2c7ac1011de66115b89b4c58',
            '_c_WBKFRo': 'pTYNdwTXsxE8FeAFsyd27Kf4gS6axlkbanoiLVw1',
            '_nb_ioWEgULi': '',
            'acw_sc__v3': '66eecaf2b9342fb077ced95af67c4b54b6742397',
            '.thumbcache_33f5730e7694fd15728921e201b4826a': 'tozNX7ujgbg/Z8tkZDPqiLCcoSyFWq+6SJIyX69IQwBcY+w3/atBAHup7s2Z70ZL4Tx0zXyx5pL50Gw7Lxl/yQ%3D%3D'
        }
        for data in datas:
            data_url = f'https://bbs.hupu.com/{data['tid']}.html'
            yield scrapy.Request(url=data_url,callback=self.get_data,cookies=cookie)
        if self.page <= 7:
            self.page += 1
            time.sleep(1)
            yield scrapy.Request(url=f'https://www.hupu.com/home/v1/news?pageNo={self.page}&pageSize=100',callback=self.parse,cookies=cookie)

    def get_data(self, response):
        """
        用于提取文章标题及其内容
        """

        title = response.xpath('//h1[@class="index_name__M5qqs"]/text()').get()
        content = response.xpath('//div[@class="thread-content-detail"]/p/text()').get()
        print(f'title:{title}\ncontent:{content}\n')
        yield {
            'title':title,
            'content':content
        }




