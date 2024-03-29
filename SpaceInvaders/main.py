import pygame
import os
import time
import random
pygame.font.init()

# Window Dimensions
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders V1")

# Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "red-ship.png"))
BLACK_SPACE_SHIP = pygame.image.load(os.path.join("assets", "black-ship.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "blue-ship.png"))

# Player player
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "green-ship.png"))

RED_LASER = pygame.image.load(os.path.join("assets", "laser.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "laser.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "laser.png"))
YELLOW_LASER  = pygame.image.load(os.path.join("assets", "laser.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

class Laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)
		
	def draw(self, window):
		window.blit(self.img, (self.x, self.y))
		
	def move(self, vel):
		self.y += vel
	
	def off_screen(self, height):
		return not(self.y <= height and self.y >= 0)

	def collision(self, obj):
		return collide(self, obj)

# Abstract class.
class Ship:
	COOLDOWN = 30

	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def	draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))
# 		pygame.draw.rect(window, (255, 0,0), (self.x, self.y, 50, 50))
		for laser in self.lasers:
			laser.draw(window)

	def move_lasers(self, vel, obj):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			elif laser.collision(obj):
				obj.health -= 10
				self.lasers.remove(laser)

	def cooldown(self):
		if self.cool_down_counter >= self.COOLDOWN:
			self.cool_down_counter = 0
		elif self.cool_down_counter > 0:
			self.cool_down_counter += 1

	def shoot(self):
		if self.cool_down_counter == 0:
			laser = Laser(self.x + 30, self.y, self.laser_img)
			self.lasers.append(laser)
			self.cool_down_counter = 1

	def get_width(self):
		return self.ship_img.get_width()

	def get_height(self):
		return self.ship_img.get_height()

class Player(Ship):
	def __init__(self, x, y, health=100):
		super().__init__(x, y, health)
		self.ship_img = GREEN_SPACE_SHIP
		self.laser_img = YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health

	def move_lasers(self, vel, objs):
		self.cooldown()
		for laser in self.lasers:
			laser.move(vel)
			if laser.off_screen(HEIGHT):
				self.lasers.remove(laser)
			else:
				for obj in objs:
					if laser.collision(obj):
						objs.remove(obj)
						if laser in self.lasers:
							self.lasers.remove(laser)

	def draw(self, window):
		super().draw(window)
		self.healthbar(window)

	def healthbar(self, window):
		pygame.draw.rect(window, (255, 0, 0),
		(self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
		pygame.draw.rect(window, (0, 255, 0),
		(self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width()
		* (self.health / self.max_health), 10))

class Enemy(Ship):
	COLOR_MAP = { 
				"red": (RED_SPACE_SHIP, RED_LASER),
				"green": (BLACK_SPACE_SHIP, GREEN_LASER),
				"blue": (BLUE_SPACE_SHIP, BLUE_LASER)
				}

	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self, vel):
		self.y += vel

def collide(obj1, obj2):
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

	 # Return a tuple with coordinate "(x, y)"
def main():
	run = True
	FPS = 60
	
	level = 0
	lives = 1
	game_over = 9
	
	main_font = pygame.font.SysFont("comicsans", 40)
	lost_font = pygame.font.SysFont("comicsans", 30)

	enemies = []
	wave_length =  4
	enemy_vel = 1

	player_vel = 5
	laser_vel = 4 

	player = Player(300, 650)

	clock = pygame.time.Clock()

	lost = False
	lost_count = 0

	def redraw_window():
		WIN.blit(BG, (0, 0))
		
		lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
		level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

		WIN.blit(lives_label, (10, 10))
		WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10 ))

		for enemy in enemies:
			enemy.draw(WIN)

		player.draw(WIN)

		if lost:
			lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
			WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width()/2, 350))

		pygame.display.update()

	while run:
	
		clock.tick(FPS)
		redraw_window()

		if player.health <= 0:
			if lives <= 1:
				lost = True
				# I think we use this if we use the bellow if lost stament which is 
				# not relevant now but need to see the tutorial again to figure out why was it done
				# lost_count += 1
				lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
				WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width()/2, 350))
				pygame.display.update()	
				time.sleep(3)
				main_menu()
			lives -= 1
			player.health = 100

# Same as comment above, check why was it done this way as the updated way works just fine
# 		if lost:
# 			if lost_count > 3 * FPS:
# 				run = False
# 			else:
# 				continue

		if len(enemies) == 0:
			if level != 0:
				if level >= game_over:
					lost_label = lost_font.render("You Win!!", 1, (255, 255, 255))
					WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width()/2, 350))
					pygame.display.update()	
					time.sleep(3)
					main_menu()
				next_round = main_font.render(f"Congrats", 1, (255, 255, 255))
				next_round2 = main_font.render(f"You passed Level: {level}", 1, (255, 255, 255))
				WIN.blit(next_round, (100, 350))
				WIN.blit(next_round2, (100, 450))

				pygame.display.update()
				pygame.time.delay(3000)
				
			level += 1
			wave_length += 3

			for i in range(wave_length):
				enemy = Enemy(random.randrange(50, WIDTH - 50), random.randrange(-800, -50),
				random.choice(["red", "blue", "green"]))
				enemies.append(enemy)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - player_vel > 0: # Left
			player.x -= player_vel
		if keys[pygame.K_d] and player.x + player_vel + player.get_height() < WIDTH: # Right
			player.x += player_vel
		if keys[pygame.K_w] and player.y - player_vel > 0: # Up
			player.y -= player_vel				
		if keys[pygame.K_s] and player.y + player_vel + player.get_width() + 15 < HEIGHT : # Down
			player.y += player_vel
		if keys[pygame.K_SPACE]: # Space
			player.shoot()

		for enemy in enemies[:]:
			enemy.move(enemy_vel)
			enemy.move_lasers(laser_vel, player)

			if random.randrange(0, 2 * 60) == 1:
				enemy.shoot()

			if collide(enemy, player):
				player.health -= 10
				enemies.remove(enemy)
			elif enemy.y + enemy.get_height() > HEIGHT:
				# Made to love 10% blood instead of one life when enemy passes the whole screen
				player.health -= 10
				enemies.remove(enemy)

		player.move_lasers(-laser_vel, enemies)

def main_menu():
	title_font = pygame.font.SysFont("comicsans", 60)
	run = True
	while run:
		WIN.blit(BG, (0,0))
		title_label = title_font.render("Press any key to start", 1, (255,255,255))
		WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))

		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				main()

	pygame.quit()	

main_menu()