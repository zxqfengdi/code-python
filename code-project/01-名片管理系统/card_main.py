# -*- coding:utf-8 -*-

"""
Name: card_main.py
Author: fengdi
Datetime: 11:20 2019/6/5
Description: 

"""

import card_tools

while True:

    # 显示功能菜单
    card_tools.show_menu()

    action_str = input("选择功能：")

    if action_str in ['1', '2', '3']:
        if action_str == '1':
            card_tools.new_card()
        elif action_str == '2':
            card_tools.show_card()
        elif action_str == '3':
            card_tools.search_card()
    elif action_str == '0':
        print("欢迎再次使用【01-名片管理系统】！")
        break
    else:
        print("输入错误，请重新输入！")
