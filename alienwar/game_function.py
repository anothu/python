import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(ai_settings,screen,ship,bullets,stats,play_button):
	#响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT and stats.game_active == True:
			sys.exit()
		if event.type == pygame.KEYDOWN and stats.game_active == True:
			check_keydown_event(event,ai_settings,screen,ship,bullets)	
		if event.type == pygame.KEYUP:
			check_keyup_event(event,ship,stats)
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(stats,play_button,mouse_x,mouse_y)

def check_play_button(stats,play_button,mouse_x,mouse_y):
	if play_button.rect.collidepoint(mouse_x,mouse_y):
		stats.game_active = True
		pygame.mouse.set_visible(False)

def check_keydown_event(event,ai_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	if event.key == pygame.K_SPACE and len(bullets) <  ai_settings.bullet_allowed:
		#创建一颗子弹
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def check_keyup_event(event,ship,stats):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	if event.key == pygame.K_p:
		stats.game_active = True
		pygame.mouse.set_visible(False)

		
def update_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,sb):
	#使用颜色背景
	screen.fill(ai_settings.bg_color)
	#放置飞船
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	if not stats.game_active:
		play_button.draw_button()
	#让最近绘制的屏幕能看见
	sb.show_score()
	pygame.display.flip()

def creat_fleet(ai_settings,screen,aliens,ship):
	#创建外星人群
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	number_available_x = get_number_aliens_x(ai_settings,alien_width)
	number_rows = get_number_rows(ai_settings,alien.rect.height,ship.rect.height)
	for row_number in range(1,number_rows):	
		for alien_number in range(number_available_x):
			creat_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
	#外星人列数
		available_space_x = ai_settings.screen_width - 2*alien_width
		number_available_x = int(available_space_x/(2*alien_width))
		return number_available_x

def get_number_rows(ai_settings,alien_height,ship_height):
	#外星人行数
	available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
	#创建一只外星人
		alien = Alien(ai_settings,screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		aliens.add(alien)


def check_fleet_edges(ai_settings,aliens):
		#有外星人到达边缘时采取相应的措施
		for alien in aliens.sprites():
			if alien.check_edges():
				change_fleet_direction(ai_settings,aliens)
				break

def change_fleet_direction(ai_settings,aliens):
		#将整群外星人下移，并改变他们的方向
		for alien in aliens.sprites():
			alien.rect.y += ai_settings.fleet_drop_speed
		ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
		#移动外星人们
		check_fleet_edges(ai_settings,aliens)
		aliens.update()
		if pygame.sprite.spritecollideany(ship,aliens):
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
		check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)


def update_bullets(bullets,ai_settings,screen,ship,aliens,stats,sb):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb):
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_score*len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)
	if len(aliens) == 0:
		stats.level += 1
		sb.prep_level()
		bullets.empty()
		ai_settings.increase_speed()
		creat_fleet(ai_settings,screen,aliens,ship)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
	#响应被外星人撞到的飞船
	if stats.ship_left > 0:
		stats.ship_left -= 1

		aliens.empty()
		bullets.empty()

		creat_fleet(ai_settings,screen,aliens,ship)
		ship.center_ship()
		sleep(0.5)
		sb.prep_ships()
	else :
		text = pygame.font.SysFont("宋体",50)
		text_fmt = text.render("you lose",1,(255,0,0))
		screen.blit(text_fmt,(0,0))
		stats.game_active = False
		pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
	#检查是否有外星人到达了底端
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
			break
def check_high_score(stats,sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
	sb.prep_score()
	sb.prep_high_score()


























