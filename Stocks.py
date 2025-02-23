import pygame
import random
import sys

class Task:
    def __init__(self, location):
        self.location = location
        self.complete = False

    def isComplete(self):
        return self.complete

    def getLocation(self):
        return self.location

    def run(self):
        pass

class Stocks(Task):
    def __init__(self, location, money):
        super().__init__(location)
        self.money = money
        self.needlePos = 300
        self.xPos = 0
        self.positions = [(self.xPos, self.needlePos)]
        self.bet = 0
        self.game_started = False
        self.previous_needle_pos = self.needlePos

    def run(self):
        pygame.init()
        width, height = 1600, 900
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Stock Market Simulation")

        font = pygame.font.SysFont(None, 36)
        bet_font = pygame.font.SysFont(None, 48)
        big_win_font = pygame.font.SysFont(None, 72)
        loser_font = pygame.font.SysFont(None, 72)
    
        fluctuationRange = 30
        clock = pygame.time.Clock()

        input_box = pygame.Rect(width // 2 + 50, height // 2 - 20, 140, 40)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''

        place_bet_text = "Place Bet"
        place_bet_surface = font.render(place_bet_text, True, pygame.Color('white'))

        while True:
            screen.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            win_condition_text = "Make $2000 to Win!"
            win_condition_surface = font.render(win_condition_text, True, pygame.Color('yellow'))
            screen.blit(win_condition_surface, (width // 2 + 50, height // 2-200))
            
            screen.blit(place_bet_surface, (width // 2 + 50, height // 2 - 60))
            pygame.draw.rect(screen, color, input_box, 2)
            txt_surface = bet_font.render(text, True, pygame.Color('white'))
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)

            money_text = f"Money: ${self.money}"
            money_surface = font.render(money_text, True, pygame.Color('white'))
            screen.blit(money_surface, (width // 2 + 50, height // 4))

            bet_text = f"Bet: ${self.bet}"
            bet_surface = font.render(bet_text, True, pygame.Color('white'))
            screen.blit(bet_surface, (width // 2 + 50, height // 3))

            

            pygame.display.flip()
            clock.tick(30)

    def reset_game(self):
        self.money = 1000
        self.bet = 0
        self.xPos = 0
        self.needlePos = 300
        self.positions = [(self.xPos, self.needlePos)]
        self.game_started = False


def main():
    test = Stocks("Stock Market", 1000)
    test.run()

if __name__ == "__main__":
    main()