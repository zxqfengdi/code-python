# -*- coding:utf-8 -*-

"""
Name: qsbk_spider.py
Author: fengdi
Datetime: 08:19 2019-08-05
Description:

"""
from urllib import request
from urllib import error
from bs4 import BeautifulSoup


# 糗事百科爬虫类
class QSBK(object):

    def __init__(self):
        self.page_index = 1
        self.url = "https://www.qiushibaike.com/hot/page/%s/"
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)" \
                          " Chrome/75.0.3770.142 Safari/537.36"
        self.headers = {"User-Agent": self.user_agent}
        self.stories = []

    # 获取页面响应
    def get_page_response(self, page_index):
        try:
            url = self.url % str(page_index)
            req = request.Request(url, headers=self.headers)
            response = request.urlopen(req)
            return response
        except error.URLError as e:
            print("连接糗事百科失败，错误原因：", e.reason)
            return

    # 获取页面段子
    def get_page_stories(self, page_index):
        response = self.get_page_response(page_index)
        if not response:
            print("页面加载失败........")
            return

        bs4obj = BeautifulSoup(response, features="lxml")
        content_list = bs4obj.find_all("div", {"class": {"article block untagged mb15 typs_hot",
                                                         "article block untagged mb15 typs_old"}})

        for content in content_list:
            author_tag = content.h2
            content_tag = content.find("div", {"class": "content"})
            image_tag = content.find("div", {"class": "thumb"})
            comment_tag = content.find("div", {"class": "likenum"})



            if not image_tag:
                author = author_tag.string.strip()
                content = content_tag.get_text().strip()
                if comment_tag:
                    comment = comment_tag.previous_sibling.replace("\n", "")
                else:
                    comment = ""

                story = "发布人：{}\n内容：{}\n神评：{}\n".format(author, content, comment)
                self.stories.append(story)

        return self.stories

    def load_page(self):
        if len(self.stories) <= 2:
            self.get_page_stories(self.page_index)
            self.page_index += 1

    def get_one_story(self):
        print(self.stories[0])
        self.stories.pop(0)

    def start(self):
        print("正在读取糗事百科，按回车查看新段子，q或Q退出")
        self.load_page()
        while True:
            info = input("请输入功能选项：")
            if info == 'q' or info == 'Q':
                break
            self.load_page()
            self.get_one_story()


def main():
    spider = QSBK()
    spider.start()


if __name__ == "__main__":
    main()

