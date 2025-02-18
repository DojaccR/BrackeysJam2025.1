class Player:
    def __inti__(self):
        self.xpos = 0
        self.ypos = 0
        self.image = pygame.image.load("Assets/Player.png")
        self.gridx = 0
        self.gridy = 0
        self.move_speed = 10

    def move(self, direction):
        if direction == "w":
            self.ypos -= self.move_speed
        elif direction == "s":
            self.ypos += self.move_speed
        elif direction == "a":
            self.xpos -= self.move_speed
        elif direction == "d":
            self.xpos += self.move_speed
        else:
            print("How did we get here?")

    def interact(self, task_list):
        for task in task_list.tasks:
            if 

    def draw(self, win):
        win.blit(self.image, (self.xpos, self.ypos))
