# -*- coding:utf-8 -*-

"""
Name: plane_main.py
Author: fengdi
Datetime: 10:35 2019-08-07
Description:

"""
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

        # 设置定时器事件（创建敌机）
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄飞机精灵及精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 添加精灵到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemy_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表是否为空
        if enemy_list:
            # 英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

    def start_game(self):
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 事件监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新绘制精灵组
            self.__update_sprites()

            # 更新显示
            pygame.display.update()


def main():
    game = PlaneGame()
    game.start_game()


if __name__ == "__main__":
    main()
