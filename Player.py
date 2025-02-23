import pygame

class Player:
    def __init__(self):
        self.xpos = 45
        self.ypos = 360
        self.image = pygame.transform.scale(pygame.image.load("Player.png"),(160,90))
        self.gridx = 0
        self.gridy = 3
        self.move_speed = 10

    def move(self, direction, room):
        if direction == "w":
            if (self.ypos - self.move_speed)//7 < self.gridx:
                if self.gridx == 0:
                    pass
                elif room.current_layout[self.gridx-1][self.gridy]==0:
                    self.ypos -= self.move_speed
                elif room.current_layout[self.gridx-1][self.gridy]==2:
                    room.change_to_file()
                elif room.current_layout[self.gridx-1][self.gridy]==3:
                    room.change_to_cp()
                else:
                    pass
            else:
                self.ypos -= self.move_speed
        elif direction == "s":
            self.ypos += self.move_speed
        elif direction == "a":
            self.xpos -= self.move_speed
        elif direction == "d":
            self.xpos += self.move_speed
        else:
            print("How did we get here?")

    def interact(self, room):
        room.interact(gridx, gridy)

    def draw(self, win):
        win.blit(self.image, (self.xpos-80, self.ypos-45))
