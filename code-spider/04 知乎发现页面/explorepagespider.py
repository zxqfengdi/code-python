# -*- coding:utf-8 -*-

"""
Name: explorepagespider.py
Author: fengdi
Datetime: 10:38 2019-08-10
Description:

"""
import time
from urllib import request
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"
headers = {
	"referer": "https://www.zhihu.com/",
	"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}


def get_page_response(url, headers):
	req = request.Request(url ,headers=headers)
	resp = request.urlopen(req)
	html_content = resp.read().decode("utf-8")
	return html_content


def get_question_info(content):
	doc = pq(content)
	question_tag_list = doc(".explore-feed.feed-item").items()
	question_index = 1

	for question in question_tag_list:
		title = question.find("h2").text()
		author = question.find(".author-link-line").text()
		content = pq(question.find(".content").html()).text()
		
		question_info = "问题：%s\n答者：%s\n回答：%s\n\n" % (title, author, content)
		
		with open("/Users/yuxi/Code/code-spider/python网络数据采集/04 知乎发现页面/question.txt", "a") as file:
			file.write(question_info)
		print("第%d条数据写入完成！" % question_index)
		question_index += 1
		time.sleep(0.5)


def main():
	print("正在爬取知乎探索页面热点内容.........")
	result = get_page_response(url, headers)
	get_question_info(result)


if __name__ == "__main__":
	main()
