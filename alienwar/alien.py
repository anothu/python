import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

	def __init__(self,ai_settings,screen):

		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载外星人图像，设置其rect属性
		self.image = pygame.image.load('image/alien.png')
		self.rect = self.image.get_rect()

		#让每个外星人出现在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#存储外星人的准确位置
		self.x = float(self.rect.x)

	def blitme(self):
		#在指定的位置绘制外星人
		self.screen.blit(self.image,self.rect)

	def update(self):
		#向右移动外星人
		self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		#如果外星人位于屏幕边缘，就返回True
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True











