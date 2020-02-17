import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
	#初始化游戏并创建一个游戏屏幕
	pygame.init()
	ai_settings = Settings()#游戏屏幕
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#屏幕宽度
	pygame.display.set_caption("Alien Invasion")#游戏名称
	#初始化飞船
	ship  = Ship(screen,ai_settings)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个用于存储外星人的编组
	aliens = Group()
	#创建外星人群
	gf.creat_fleet(ai_settings,screen,aliens,ship)
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	play_button = Button(ai_settings,screen,"Play")
	sb = Scoreboard(ai_settings,screen,stats)

	#开始游戏的主循环
	while True:
		#监听鼠标，键盘事件	
			gf.check_events(ai_settings,screen,ship,bullets,stats,play_button)
			if stats.game_active:
				ship.update()
				gf.update_bullets(bullets,ai_settings,screen,ship,aliens,stats,sb)
				gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)
				print(len(bullets)) 
			gf.update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb)
		
run_game()