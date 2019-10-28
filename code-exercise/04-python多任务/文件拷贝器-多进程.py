# -*- coding:utf-8 -*-

"""
Name: 文件拷贝器-多进程.py
Author: fengdi
Datetime: 5:12 下午 2019/10/28
Description: 
"""

import os
from multiprocessing import Pool


def copy_file(dest_path, name, copy_file_path):
	with open(dest_path + '/' +  name, 'rb') as file:
		file_content = file.read()
		with open(copy_file_path + '/' +  name, 'wb') as new_file:
			new_file.write(file_content)

	print("目标文件：%s拷贝完成！" % (dest_path + name))


def main():

	# 获取目标目录路径
	dest_path = input("请输入要复制的目录名：")

	# 获取目录内所用内容
	all_file = os.listdir(dest_path)

	# 当前目录创建放置复制文件的新目录
	copy_file_path = 'test[复件]'

	if not os.path.exists(copy_file_path):
		os.mkdir(copy_file_path)

	# 创建进程池
	pool = Pool(5)

	# 复制内容
	for name in all_file:
		pool.apply_async(copy_file, args=(dest_path, name, copy_file_path))

	pool.close()
	pool.join()


if __name__ == '__main__':
	main()