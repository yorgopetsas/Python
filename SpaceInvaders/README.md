# Making an	abstract class. Those are clases you don't actually use, but you inherit from them
class Ship:


		# When drawing rectangle we can define width at the end and it will make border, 
		# otherways it will create the rectangle filled with the selected color. 
		# Ex: pygame.draw.rect(window, (255, 0,0), (self.x, self.y, 50, 50), 2) 
		# This will produce rectangle with border of 2 px 
		
/
		# if we use "event.type == pygame.KEYDOWN" only one key will be detected per loop (FPS times a second)
		# This is why we use 		keys = pygame.key.get_pressed()
