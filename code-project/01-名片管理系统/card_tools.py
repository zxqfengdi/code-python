# -*- coding:utf-8 -*-

"""
Name: card_tools.py
Author: fengdi
Datetime: 11:20 2019/6/5
Description: 

"""

# 用户名片列表
user_list = []


def show_menu():
	"""
	显示功能菜单
	:return: 无返回值
	"""
	print("*" * 50)
	print("欢迎使用【01-名片管理系统】 V1.0\n")
	print("1. 新建名片\n2. 显示名片\n3. 查询名片\n\n0. 退出系统")
	print("*" * 50)


def new_card():
	"""
	新建名片操作
	:return: 无返回值
	"""
	print("请输入用户名片信息：")

	name = input("姓名:")
	phone = input("电话：")
	qq = input("QQ：")
	email = input("邮箱：")

	user_dict = {'name': name, 'phone': phone, 'qq': qq, 'email': email}
	user_list.append(user_dict)
	print("用户%s添加成功！" % name)


def show_card():
	"""
	显示名片操作
	:return: 无返回值
	"""
	if len(user_list) == 0:
		print("名片不存在，请先添加名片！")
	else:
		for info in ["姓名", '电话', 'QQ', '邮箱']:
			print(info, end='\t\t')
		print("")
		print("=" * 80)
		for user_dict in user_list:
			print("%s\t\t%s\t\t%s\t\t%s" % (user_dict['name'], user_dict['phone'], user_dict['qq'], user_dict['email']))


def search_card():
	"""
	查询名片操作
	:return: 无返回值
	"""
	find_name = input("请输入要查询的用户名字:")

	for user_dict in user_list:
		if user_dict['name'] == find_name:
			# 找到用户进行后续处理
			deal_card(user_dict)
			break
	else:
		print("未找到该用户，请重新输入！")


def deal_card(card):
	"""
	对找到的名片进行修改和删除操作
	:param card: 找到的名片字典
	:return: 无返回值
	"""
	print("用户%s已找到！" % card['name'])

	for info in ["姓名", '电话', 'QQ', '邮箱']:
		print(info, end='\t\t')
	print("")
	print("=" * 80)
	print("%s\t\t%s\t\t%s\t\t%s" % (card['name'], card['phone'], card['qq'], card['email']))

	action_str = input("功能选择：1 修改 2 删除 0 返回上级菜单:")

	if action_str == '1':
		card['name'] = my_input(card['name'], "姓名:")
		card['phone'] = my_input(card['phone'], "电话:")
		card['qq'] = my_input(card['qq'], "QQ:")
		card['email'] = my_input(card['email'], "邮箱:")
	elif action_str == '2':
		user_list.remove(card)
		print("用户%s删除成功！" % card['name'])


def my_input(card_value, tip_message):
	"""
	重新定义输入函数
	:param card_value: 原名片字典值
	:param tip_message: 提示信息
	:return: 用户输入值，则返回其输入值；否则返回名片字典原有值
	"""
	info_str = input(tip_message)

	if len(info_str) > 0:
		return info_str
	else:
		return card_value


if __name__ == "__main__":
	pass
