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
    
        clock = pygame.time.Clock()

        input_box = pygame.Rect(width // 2 + 50, height // 2 - 20, 140, 40)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''

        place_bet_surface = font.render("Place Bet", True, pygame.Color('white'))

        while True:
            screen.fill((0, 0, 0))
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                        color = color_active
                    else:
                        active = False
                        color = color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if text.isdigit() and int(text) <= self.money:
                                self.bet = int(text)
                                self.money -= self.bet
                                self.game_started = True
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.blit(place_bet_surface, (width // 2 + 50, height // 2 - 60))

            pygame.draw.rect(screen, color, input_box, 2)
            txt_surface = bet_font.render(text, True, pygame.Color('white'))
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)

            money_surface = font.render(f"Money: ${self.money}", True, pygame.Color('white'))
            screen.blit(money_surface, (width // 2 + 50, height // 4))

            bet_surface = font.render(f"Bet: ${self.bet}", True, pygame.Color('white'))
            screen.blit(bet_surface, (width // 2 + 50, height // 3))

            if self.money <= 0:
                loser_surface = loser_font.render("LOSER!", True, pygame.Color('red'))
                screen.blit(loser_surface, (width // 2 - loser_surface.get_width() // 2, height // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                self.reset_game()
                continue

            if self.money >= 2000:
                big_win_surface = big_win_font.render("Big Wins!", True, pygame.Color('green'))
                screen.blit(big_win_surface, (width // 2 - big_win_surface.get_width() // 2, height // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()

            if self.game_started:
                self.game_loop(screen, clock, width, height)

            pygame.display.flip()
            clock.tick(30)

    def game_loop(self, screen, clock, width, height):
        fluctuationRange = 10
        while self.xPos < width // 2:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            marketTrend = random.choice([1, -1])
            fluctuation = random.randint(0, fluctuationRange) * marketTrend

            self.needlePos += fluctuation
            if self.needlePos < 0:
                self.needlePos = 0
            elif self.needlePos > height:
                self.needlePos = height

            self.previous_needle_pos = self.needlePos

            xFluctuation = random.randint(1, 5)
            self.xPos += xFluctuation

            self.positions.append((self.xPos, self.needlePos))

            for i in range(1, len(self.positions)):
                pygame.draw.line(screen, (255, 0, 0), self.positions[i-1], self.positions[i], 2)

            font = pygame.font.SysFont(None, 36)
            money_surface = font.render(f"Money: ${self.money}", True, pygame.Color('white'))
            screen.blit(money_surface, (width // 2 + 50, height // 4))

            bet_surface = font.render(f"Bet: ${self.bet}", True, pygame.Color('white'))
            screen.blit(bet_surface, (width // 2 + 50, height // 3))

            pygame.display.flip()
            clock.tick(30)

        self.end_game()

    def end_game(self):
        movement = self.needlePos - 300
    
        if movement > 0:
            self.money += self.bet * (1 + movement / 100)
        elif movement < 0:
            self.money -= self.bet

        self.bet = 0
        self.xPos = 0
        self.needlePos = 300
        self.positions = [(self.xPos, self.needlePos)]
        self.game_started = False

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
