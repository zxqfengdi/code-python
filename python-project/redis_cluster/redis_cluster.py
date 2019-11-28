# -*- coding:utf-8 -*-

"""
Name: redis_cluster.py
Author: fengdi
Datetime: 3:46 下午 2019/11/28
Description: python操作redis集群
"""

from rediscluster import *

if __name__ == '__main__':
    try:
        # 构建所有的主节点，Redis会使⽤CRC16算法，将键和值写到某个节点上
        startup_nodes = [
            {'host': '172.17.0.9', 'port': 7000},
            {'host': '172.17.0.9', 'port': 7001},
            {'host': '172.17.0.9', 'port': 7002},
        ]

        # 构建StrictRedisCluster对象
        src = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

        # 设置键值对
        result = src.set('name', '中国')
        print(result)

        # 获取
        name = src.get('name')
        print(name)

    except Exception as e:
        print(e)
