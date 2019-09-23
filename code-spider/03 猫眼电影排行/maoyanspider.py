# -*- coding:utf-8 -*-

"""
Name: maoyanspider.py
Author: fengdi
Datetime: 19:16 2019-08-06
Description:

"""
import re
import time
import requests

class CatMovie(object):

    def __init__(self):
        self.page_index = 0
        self.count = 1
        self.base_url = "https://maoyan.com/board/4?offset=%s"
        self.headers = {
            "Host": "maoyan.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        self.move_info_list = []

    def get_response(self, page_url):
        try:
            response = requests.get(page_url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print("获取网页内容出现异常：", e)
        else:
            return response

    def get_movie_info(self, page_index):
        page_url = self.base_url % str(page_index)
        response = self.get_response(page_url)
        html_content = response.text
        pattern = r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>' \
                  r'(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
        match_list = re.findall(pattern, html_content, re.S)

        for match in match_list:
            movie_info = "序号：%s\n封面链接：%s\n名称：%s\n%s\n%s\n评分：%s\n\n" % \
                         (match[0].strip(), match[1].strip(), match[2].strip(), match[3].strip(), match[4].strip(),
                          match[5].strip() + match[6].strip())
            self.move_info_list.append(movie_info)

        self.page_index += 10

    def load_page(self):
        if len(self.move_info_list) <= 2:
            self.get_movie_info(self.page_index)

    def write_movieinfo_to_file(self):
        movie_info = self.move_info_list[0]
        print("正在写入第%d条数据........." % self.count)
        with open("./movie_info.txt", "a") as f:
            f.write(movie_info)
        print("第%d条数据写入成功！！" % self.count)
        self.count += 1
        self.move_info_list.pop(0)
        time.sleep(0.5)

    def start(self):
        print("正在读取猫眼电影排行榜............")
        # 加载一页内容
        self.load_page()
        while True:
            self.write_movieinfo_to_file()
            self.load_page()
            if len(self.move_info_list) == 0:
                break


def main():
    spider = CatMovie()
    spider.start()


if __name__ == '__main__':
    main()

