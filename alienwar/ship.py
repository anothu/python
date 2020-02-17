import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self,screen,ai_settings):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船位图信息
		self.image = pygame.image.load('image/ship.png')
		self.rect = self.image.get_rect()#获取游戏元素信息
		self.screen_rect = screen.get_rect()#获得游戏屏幕信息
		
		#将每艘飞船放在屏幕 底部 中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.centerx = float(self.rect.centerx)
		#移动标志
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		#根据移动标志调整飞船的位置
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += float(self.ai_settings.ship_speed_factor)		
		if self.moving_left and self.rect.left > 0:
			self.centerx -= float(self.ai_settings.ship_speed_factor)
		self.rect.centerx = self.centerx

	def blitme(self):
        #在指定位置放置飞船
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		#让飞船在屏幕中居中
		self.center = self.screen_rect.centerx