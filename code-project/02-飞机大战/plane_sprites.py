# -*- coding:utf-8 -*-

"""
Name: plane_sprites.py
Author: fengdi
Datetime: 10:36 2019-08-07
Description:

"""

import random
import pygame

# 设置游戏窗口常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 设置刷新帧率
FRAME_PER_SEC = 60

# 设置创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 游戏主类
class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):

        # 调用父类初始化方法
        super().__init__()

        # 定义游戏精灵属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


# 背景精灵类
class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# 敌机精灵类
class Enemy(GameSprite):

    def __init__(self):
        super().__init__('./images/enemy1.png')

        # 指定敌机初始随机速度
        self.speed = random.randint(1, 3)

        # 指定敌机初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):

        # 调用父类方法保持垂直方向移动
        super().update()

        # 判断敌机是否飞出屏幕，若飞出，从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


# 英雄飞机精灵类
class Hero(GameSprite):

    def __init__(self):

        super().__init__('./images/me1.png', 0)

        # 设置飞机初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        # 判断英雄飞机位置
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in (0, 1, 2):

            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            self.bullet_group.add(bullet)


# 子弹精灵类
class Bullet(GameSprite):

    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self):

        super().update()

        if self.rect.bottom < 0:
            self.kill()

def main():
    pass


if __name__ == "__main__":
    main()
