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
            if ((self.ypos - self.move_speed)//(720/7)) < self.gridy:
                print("changegrid")
                if self.gridy == 0:
                    print("worldborder")
                    pass
                elif room.current_layout[self.gridy-1][self.gridx]==0:
                    self.ypos -= self.move_speed
                    self.gridy -= 1
                elif room.current_layout[self.gridy-1][self.gridx]==2:
                    room.change_to_file()
                elif room.current_layout[self.gridy-1][self.gridx]==3:
                    room.change_to_cp()
                    self.xpos = 45
                    self.ypos = 360
                    self.gridx = 0
                    self.gridy = 3
                else:
                    print(room.current_layout[self.gridy-1][self.gridx])
                    print("table")
                    pass
            else:
                self.ypos -= self.move_speed
        elif direction == "s":
            if ((self.ypos + self.move_speed)//(720/7)) > self.gridy:
                print("changegrid")
                if self.gridy == 6:
                    print("worldborder")
                    pass
                elif room.current_layout[self.gridy+1][self.gridx]==0:
                    self.ypos += self.move_speed
                    self.gridy += 1
                elif room.current_layout[self.gridy+1][self.gridx]==2:
                    room.change_to_file()
                elif room.current_layout[self.gridy+1][self.gridx]==3:
                    room.change_to_cp()
                    self.xpos = 45
                    self.ypos = 360
                    self.gridx = 0
                    self.gridy = 3
                else:
                    print(room.current_layout[self.gridy+1][self.gridx])
                    print("table")
                    pass
            else:
                self.ypos += self.move_speed
        elif direction == "a":
            if ((self.xpos - self.move_speed)//(720/7)) < self.gridx:
                print("changegrid")
                if self.gridx == 0:
                    print("worldborder")
                    pass
                elif room.current_layout[self.gridy][self.gridx-1]==0:
                    self.xpos -= self.move_speed
                    self.gridx -= 1
                elif room.current_layout[self.gridy][self.gridx-1]==2:
                    room.change_to_file()
                elif room.current_layout[self.gridy][self.gridx-1]==3:
                    room.change_to_cp()
                    self.xpos = 45
                    self.ypos = 360
                    self.gridx = 0
                    self.gridy = 3
                else:
                    print(room.current_layout[self.gridy][self.gridx-1])
                    print("table")
                    pass
            else:
                self.xpos -= self.move_speed
        elif direction == "d":
            if ((self.xpos + self.move_speed)//(1280/13)) > self.gridx:
                print("changegrid")
                if self.gridx == 12:
                    print("worldborder")
                    pass
                elif room.current_layout[self.gridy][self.gridx+1]==0:
                    self.xpos += self.move_speed
                    self.gridx += 1
                elif room.current_layout[self.gridy][self.gridx+1]==2:
                    room.change_to_file()
                elif room.current_layout[self.gridy][self.gridx+1]==3:
                    room.change_to_cp()
                    self.xpos = 45
                    self.ypos = 360
                    self.gridx = 0
                    self.gridy = 3
                else:
                    print(str(room.current_layout[self.gridy][self.gridx+1]) +" at " + str(self.gridx) + ":" + str(self.gridy))
                    print("table")
                    pass
            else:
                self.xpos += self.move_speed
        else:
            print("How did we get here?")

    def interact(self, room):
        room.interact(self.gridx, self.gridy)

    def draw(self, win):
        win.blit(self.image, (self.xpos-80, self.ypos-45))
