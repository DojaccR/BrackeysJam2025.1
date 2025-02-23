import pygame

class Room:
    def __init__(self):
        self.computer_tasks = [0,0,0,0,0] # five tasks all set to false in initialisation of class
        self.computer_tasks_coords = [(),(),(),(),()]
        self.shred_tasks = [0,0,0,0,0]
        self.shred_tasks_coords = [(),(),(),(),()]
        self.sort_tasks = [0,0,0,0,0]
        self.sort_tasks_coords = [(1,5),(7,2),(),(),()]
        self.current_room = 0 # Roomtypes 0 for main, 1 for computer, 2 for file room
        self.room_textures = [pygame.image.load("Office.jpeg"), pygame.image.load("FileRoom.jpeg"), pygame.image.load("CompRoom.jpeg")]
        self.office_layout = [
        [1,1,1,1,1,2,2,2,1,0,1,0,3],
        [0,1,1,1,1,9,0,0,0,0,0,0,3],
        [0,0,0,0,0,0,0,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,1,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,1,1,1,1,0]
        ]
        self.file_layout = []
        self.cp_layout  = [
        [0,0,0,1,1,1,1,0,0,0,1,1,1],
        [0,0,0,1,1,1,1,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,0,1,1,1,1,1,0,1,0,1,1,1]
        ]
        self.current_layout = self.office_layout
    
    def generate_tasks(self,day):
        self.computer_tasks = [0,0,0,0,0] # making all tasks false, not necessary but whatever
        self.shred_tasks = [0,0,0,0,0]
        self.sort_tasks = [0,0,0,0,0]
        for i in randge(day):
            self.computer_task[i] = 1
            self.shred_task[i] = 1
            self.sort_task[i] = 1
        

    def new_day(self,day):
        self.generate_tasks(day)


    def interact(self, grix, gridy):
        adjacent = [(gridx + 1, gridy),(gridx - 1, gridy),(gridx, gridy + 1),(gridx, gridy - 1)]
        if self.current_room == 0:
            for block in adjacent:
                if block == adjacent:
                    pass
        elif self.current_room == 1:
            pass
        elif self.current_room == 2:
            pass
    
    def change_to_file(self):
        self.current_room = 1
        self.current_layout = self.file_layout

    def change_to_cp(self):
        self.current_room = 2
        self.current_layout = self.cp_layout

    def change_to_office(self):
        self.current_room = 0
        self.current_layout = self.office_layout

    def complete(self):
        if sum(self.computer_tasks) + sum(self.shred_tasks) + sum(self.sort_tasks) == 0:
            return True
        else:
            return False


    def draw(self,win):
        if self.current_room==0:
            win.blit(self.room_textures[0],(0,0))
            for task in self.sort_tasks:
                pass
        elif self.current_room == 1:
            win.blit(self.room_textures[1],(0,0))
            for task in self.computer_tasks:
                pass
        elif self.current_room == 2:
            win.blit(self.room_textures[2],(0,0))
            for task in self.shred_tasks:
                pass
