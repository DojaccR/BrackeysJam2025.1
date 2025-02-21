import pygame

class Game:
	def __init__(self, win):
		self.day = 0 # Tracks days of avoiding fraud
		self.tick = 0 # Tracks ticks per day
		self.win = win # window to draw to
		self.current_room = 0 # The room with the player in it
		self.task_list = Tasklist.Tasklist() # Task list object to track tasks

	def run(self):
        # Keeps track of time
        self.tick+=1
        # When tick = 200 a day is complete and we need
        # to do checks for win and set up new day.
        if self.tick == 200:
            self.tick = 0
            if task_list.complete():
                self.day += 1
            else:
                return False

        # Take user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            # Player Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_w:
                    self.player.move(w)
                if event.key == pygame.K_s:
                    self.player.move(s)
                if event.key == pygame.K_a:
                    self.player.move(a)
                if event.key == pygame.K_d:
                    self.player.move(d)
            # Player interaction with environmnt
                if event.key == pygame.K_e:
                    self.player.interact()
        # Drawing to window
        self.room.draw(self.win)
        self.player.draw(self.win)
        pygame.display.flip()
