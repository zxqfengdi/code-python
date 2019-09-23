# -*- coding:utf-8 -*-

"""
Name: meizitu_spider.py
Author: fengdi
Datetime: 12:54 2019-08-05
Description:

"""
from urllib import request
from lxml import etree
import time

base_url = "https://www.mzitu.com/page/%s/"
headers = {
    "referer": "https://www.mzitu.com/",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}

def get_page_response(url, headers):
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    html_content = resp.read()
    return html_content

def get_img_url(html_content):
    html = etree.HTML(html_content)
    img_name_list = html.xpath("//ul[@id='pins']/li/a/img/@alt")
    img_url_list = html.xpath("//ul[@id='pins']/li/a/img/@data-original")

    return zip(img_name_list, img_url_list)

def write_image_to_file(index, name, html_data):
    img_name = name + '.jpg'
    with open("/Volumes/Data/spider_data/meizitu_image" + '/' + img_name,  "wb") as file:
        file.write(html_data)
    print("写入第%d张图片------>%s写入完成!" % (index, img_name))

def main():
    print("正在爬取妹子图........")
    img_index = 1
    for i in range(1, 228):
        url = base_url % i
        html_content = get_page_response(url, headers)
        img_info = get_img_url(html_content)
        for name, url in img_info:
            html_content = get_page_response(url, headers)
            write_image_to_file(img_index, name, html_content)
            img_index += 1
            time.sleep(0.5)
        time.sleep(1)


if __name__ == "__main__":
    main()