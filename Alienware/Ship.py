import pygame

class Ship():
    def __init__(self,screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        
        # 加载飞船图像并获取外接矩形
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将飞船放在屏幕底部
        self.rect.centerx = slef.screen_rect.cneterx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitem(self):
        """ 在指定位置设置绘制飞船"""
        self.screen.blit(self.image,self.rect)
        
        