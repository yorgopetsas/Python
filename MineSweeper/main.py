import pygame
import random
from multiprocessing import Queue
pygame.init()

WIDTH, HEIGHT = 700, 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MineSweeper V1.0")

BG_COLOR= "white"
ROWS, COLS = 15, 15
MINES = 15

SIZE = 	WIDTH / ROWS

NUM_FONT = pygame.font.SysFont('comicsans', 20)
NUM_COLORS = {1: "black", 2: "green", 3: "red", 4: "orange", 5: "yellow", 6: "purple", 7: "blue", 8: "pink"}
RECT_COLOR = (200, 200, 200)
CLICKED_RECT_COLOR  = (140, 140, 140)
FLAG_RECT_COLOR = "red"

def get_neighbors(row, col, rows, cols):
	neighbors = []
	
	if row > 0: #UP
		neighbors.append((row - 1, col))
	if row < rows - 1: #DOOM
		neighbors.append((row + 1, col))
	if col > 0: # LEFT
		neighbors.append((row, col - 1))
	if col < cols - 1: #RIGHT
		neighbors.append((row, col + 1))

	
	if row > 0 and col > 0:
		neighbors.append((row - 1, col - 1))
	if row < rows - 1 and col < cols - 1:
		neighbors.append((row + 1, col + 1))
	if row < rows - 1 and col > 0:
		neighbors.append((row + 1, col - 1))	
	if row > 0 and col < cols - 1:
		neighbors.append((row - 1, col + 1))	
	
	return neighbors


def create_mine_field(rows, cols, mines):
	field= [[0 for _ in range(cols)] for _ in range(rows)]
	mine_positions = set()
	
	while len(mine_positions) < mines:
		row = random.randrange(00, rows)
		col = random.randrange(00, cols)
		pos = row, col
		 
		if pos in mine_positions:
			continue
		  
		mine_positions.add(pos)
		field[row][col] = -1
		
	for mine in mine_positions:
		neighbors= get_neighbors(*mine, rows, cols)
		for r, c in neighbors:
			field[r][c] += 1
	
	return field

def draw(win, field, cover_field):
	win.fill(BG_COLOR)

	for i, row in enumerate(field):
		y = SIZE * i
		for j, value in enumerate(row):
			x = SIZE * j
			
			is_covered = cover_field[i][j] == 0
			is_flag = cover_field[i][j] == -2
			
			if is_flag == -2:
				pygame.draw.rect(win, FLAG_RECT_COLOR, (x, y, SIZE, SIZE))
				pygame.draw.rect(win, "black", (x, y, SIZE, SIZE), 2)
				continue
			
			if is_covered:
				pygame.draw.rect(win, RECT_COLOR, (x, y, SIZE, SIZE))
				pygame.draw.rect(win, "black", (x, y, SIZE, SIZE), 2)
				continue
			else:
				pygame.draw.rect(win, CLICKED_RECT_COLOR, (x, y, SIZE, SIZE))
				pygame.draw.rect(win, "black", (x, y, SIZE, SIZE), 2)
						
			if value > 0:	
				text = NUM_FONT.render(str(value), 1, NUM_COLORS[value])
				win.blit(text, (x + (SIZE/2 - text.get_width()/2),
								y + (SIZE/2 - text.get_height()/2)))	

	pygame.display.update()

def get_grid_pos(mouse_pos):
	mx, my = mouse_pos
	row = int(my // SIZE)
	col = int(mx // SIZE)
	
	return row, col

def uncover_from_pos(row, col, cover_field, field):
	q = Queue()
	q.put((row, col))
	visited = set()
	
	while not q.empty():
		current = q.get()
		
		neighbors = get_neigbors(*current, ROWS, COLS)
		for r, c in neighbors:
			if (r, c) in visited:
				continue
			value = field[r][c]
			cover_field[r][c] = 1
			if value == 0:
				q.put((r, c))
			
			visited.add((r, c))

def main(win):
	run = True
	field = create_mine_field(ROWS, COLS, MINES)
	cover_field = [[0 for _ in range(COLS)] for _ in range(ROWS)]
# 	flag_positions = set()
	flags = MINES
	
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				row, col = get_grid_pos(pygame.mouse.get_pos())
				if row >= ROWS or col >= COLS:
					continue				

				mouse_pressed = pygame.mouse.get_pressed()
				if mouse_pressed[0]:		
					cover_field[row][col] = 1
					uncover_from_pos(row, col, cover_field, field)
				elif mouse_pressed[2]:
					if cover_field[row][col] == -2:
						cover_field[row][col] = 0
						flags += 1
					else:
						flags -= 1
						cover_field[row][col] = -2
 					
		draw(win, field, cover_field)

	pygame.quit()

if __name__ == "__main__":
	main(win)
	
# In "neighbors= get_neighbors(*mine, rows, cols)" what does the * astrix do - decompose (mine?) - what does it mean?
# In "pygame.draw.rect(win, "black", (x, y, SIZE, SIZE), 2)" The last 2 sets the thinkness
# Needed to import from multiprocessing import Queue not Queue