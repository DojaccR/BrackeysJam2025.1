import pygame
import Room
import Player

class Game:
    def __init__(self, win, clock):
        self.day = 0 # Tracks days of avoiding fraud
        self.tick = 0 # Tracks ticks per day
        self.win = win # window to draw to
        self.room = Room.Room() # The room with the player in it
        self.player = Player.Player()
        self.clock = pygame.time.Clock
    
    def next_day(self,day):
        self.room.new_day(day)

    def run(self):
        while(True):
            # Keeps track of time
            pygame.time.delay(20)
            self.tick+=1
            # When tick = 200 a day is complete and we need
            # to do checks for win and set up new day.
            if self.tick == 6000:
                self.tick = 0
                if self.room.complete():
                    self.next_day(self.day + 1)
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
                # Player interaction with environmnt
                    if event.key == pygame.K_e:
                        self.player.interact()
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                self.player.move('w',self.room)
            if key[pygame.K_s]:
                self.player.move('s',self.room)
            if key[pygame.K_a]:
                self.player.move('a',self.room)
            if key[pygame.K_d]:
                self.player.move('d',self.room)
        # Drawing to window
            self.room.draw(self.win)
            self.player.draw(self.win)
            pygame.display.flip()
