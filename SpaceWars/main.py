import pygame
import os

# We need this in order to print/render text on the screen
#
pygame.font.init()

# Unit for sound playback
#
pygame.mixer.init ()

# We are setting several global variables. We use the CAPS as per good practice to 
# differentiate from the rest of the variables

# DIMENSION & OTHERS
#
WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 80, 80

# FRAMES PER SECOND, VELOCITY and other characteristics
#
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
BORDER = pygame.Rect(WIDTH//2 - 4, 0, 8, HEIGHT)

# EVENTS: Create custom user event. Must assign a different ID for each event Ex: "+1"
#
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# COLORS & STYLE
#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0) 
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 120)

# ASSESTS
#
YELLOW_SPACESHIP_URL = "spaceship-black.png"
RED_SPACESHIP_URL = "spaceship-green.png"
SPACE = pygame.transform.scale(pygame.image.load(
	os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# SOUNDS
#
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hit.wav'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'fire.wav'))

# Setting up the game window
#
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting up the windos caption
#
pygame.display.set_caption("Space Wars 2023")

# Load the spaceship images from a file with the load method of the image Class
# Use the methods Scale and Rotate (from the transform Class) to finetune the images
#
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
	os.path.join('Assets', YELLOW_SPACESHIP_URL))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
	YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

RED_SPACESHIP_IMAGE = pygame.image.load(
os.path.join('Assets', RED_SPACESHIP_URL))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
	RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

# The draw_window() function is taking care of displaying the objects (background, spaceships, bullets)
#
def draw_window(yellow, red, red_bullets, yellow_bullets, yellow_health, red_health):
	#Template (background, border, stats)
	#
	WIN.blit(SPACE, (0, 0))
	pygame.draw.rect(WIN, WHITE, BORDER)
	yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
	red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
	WIN.blit(yellow_health_text, (10, 10))
	WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))

	#Draw Ships
	#
	WIN.blit(YELLOW_SPACESHIP , (yellow.x, yellow.y))
	WIN.blit(RED_SPACESHIP, (red.x, red.y))
	
	#Draw Bullets
	#
	for bullet in red_bullets:
		pygame.draw.rect(WIN, RED, bullet)

	for bullet in yellow_bullets:
		pygame.draw.rect(WIN, YELLOW, bullet)
		
	pygame.display.update()

#Draw Game Over Text
#
def draw_winner(text):
	if text == "Yellow wins!":
		winner_color = YELLOW
	if text == "Red wins!":
		winner_color = RED
		
	draw_text = WINNER_FONT.render(text, 1, winner_color)
	WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
	pygame.display.update()
	pygame.time.delay(5000)

# With this functions we track the pressed keys and update the position of the spaceships
# There are additional conditions so we can make sure this spaceship can only move in his
# half of the screen. Not crossing to the other field nor going outside of the window.
#
def yellow_ship_movement(keys_pressed, yellow):
	if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
		yellow.x -= VEL
	if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT
		yellow.x += VEL
	if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
		yellow.y -= VEL
	if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: # DOWN
		yellow.y += VEL	

def red_ship_movement(keys_pressed, red):
	if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # LEFT
		red.x -= VEL
	if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - SPACESHIP_WIDTH: # RIGHT
		red.x += VEL
	if keys_pressed[pygame.K_UP] and red.y - VEL > 0: # UP
		red.y -= VEL
	if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT: # DOWN
		red.y += VEL

# Control amount of bullets, check for collusion
# Posting an event so we can check for it in the main function!
#
def hadnle_bullets(yellow_bullets, red_bullets, yellow, red):
	for bullet in yellow_bullets:
		bullet.x += BULLET_VEL
		if red.colliderect(bullet):
			pygame.event.post(pygame.event.Event(RED_HIT))
			yellow_bullets.remove(bullet)
		elif bullet.x > WIDTH:
			yellow_bullets.remove(bullet)

	for bullet in red_bullets:
		bullet.x -= BULLET_VEL
		if yellow.colliderect(bullet):
			pygame.event.post(pygame.event.Event(YELLOW_HIT))
			red_bullets.remove(bullet)
		elif bullet.x < 0:
			red_bullets.remove(bullet)


	
def main():
	yellow = pygame.Rect(50, 210, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	red = pygame.Rect(780, 210, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

	yellow_bullets = []
	red_bullets = []
	
	red_health = 9
	yellow_health = 9	
	
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			#Check and end game if user quits
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				
			# BULLET EVENTS
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
					yellow_bullets.append(bullet)
					BULLET_FIRE_SOUND.play()
					
				if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
					red_bullets.append(bullet)
					BULLET_FIRE_SOUND.play()
					
			if event.type == RED_HIT:
				red_health -= 1
				BULLET_HIT_SOUND.play()
				
			if event.type == YELLOW_HIT:
				yellow_health -= 1
				BULLET_HIT_SOUND.play()
						
		winner_text = ""
		if red_health <= 0:
			winner_text = "Yellow wins!"
		if yellow_health <= 0:
			winner_text = "Red wins!"
		
		if winner_text != "":
			draw_winner(winner_text)
			break
		
		keys_pressed = pygame.key.get_pressed()
		yellow_ship_movement(keys_pressed, yellow)
		red_ship_movement(keys_pressed, red)
		hadnle_bullets(yellow_bullets, red_bullets, yellow, red)
		draw_window(yellow, red, red_bullets, yellow_bullets, yellow_health, red_health)

	main()

# Making sure the program can be executed only from this file. 
# Not so important for this project but an important habbit
#
if __name__ == "__main__":
	main()