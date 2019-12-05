# -*- coding:utf-8 -*-

"""
Name: friends_info_visualization.py
Author: fengdi
Datetime: 10:40 上午 2019/12/4
Description: 微信朋友信息可视化
"""
import itchat

itchat.auto_login(hotReload=True)

friends_list = itchat.get_friends()

friends_info_list = []

for friends in friends_list:
    friends_info = dict()

    friends_info['备注'] = friends['RemarkName']
    friends_info['性别'] = friends['Sex']
    friends_info['个性签名'] = friends['Signature']
    friends_info['省份'] = friends['Province']
    friends_info['城市'] = friends['City']

    friends_info_list.append(friends_info)


for info in friends_info_list:
    print(info)


