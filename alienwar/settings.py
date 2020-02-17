class Settings():

	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (255,255,255)
		self.ship_speed_factor = 9
		self.ship_limit = 3
		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 10
		#外星人设置
		self.alien_speed_factor = 5
		self.fleet_drop_speed = 10
		self.alien_score = 50
		self.score_speedup_scale = 1.5
		#fleet-direction为1向右移，-1向左移动
		self.fleet_direction = 1
		#加快游戏节奏
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 4.5
		self.bullet_speed_factor = 5
		self.alien_speed_factor = 10

		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale 
		self.alien_score *= int(self.score_speedup_scale)
		




