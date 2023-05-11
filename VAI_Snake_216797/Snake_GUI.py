from Snake import SnakeGame
import pygame
from pygame.locals import *
import time
import random

rand = random.Random()

class SnakeGameGUI(SnakeGame):
    
    def __init__(self, headless_mode = False):
        pygame.init()
        super().__init__()
        self.BLUE = (200, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (76,153,0)
        width = pygame.display.Info().current_w
        self.SNKHEAD = pygame.image.load("Img/Snake_Head.png")
        self.SNKHEAD = pygame.transform.scale(self.SNKHEAD, ((width/40)*1.8,(width/40)*1.8))
        self.APPLE = pygame.image.load("Img/Apple.png")
        self.APPLE = pygame.transform.scale(self.APPLE, ((width/40),(width/40)))
        pygame_icon = pygame.image.load("Img/Snake_Head.png")
        pygame.display.set_icon(pygame_icon)
        pygame.display.set_caption("Snake Game!")
        self.SQUARESIZE = (width/40)

        if headless_mode == False:
            self.SCREEN = pygame.display.set_mode((width*0.5, width*0.5))
            pygame.init()

    def draw_board(self):
        myfont2 = pygame.font.SysFont("monospace", 20)
        self.SCREEN.fill(self.BLUE)
        for x in range(0, 20, 2):
            for y in range(0, 20, 2):
                pygame.draw.rect(self.SCREEN, (210, 255, 255), (x*self.SQUARESIZE, y*self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
        for i in range(self.height):
            for j in range(self.width):
                # Body
                if self.board[i, j] == 1:
                    loc_size = (j*self.SQUARESIZE, i*self.SQUARESIZE, self.SQUARESIZE*1.02, self.SQUARESIZE*1.02)
                    pygame.draw.rect(self.SCREEN, self.GREEN, loc_size)
                # Head
                elif self.board[i, j] == 2:
                    loc = ((j*self.SQUARESIZE)-self.SQUARESIZE*0.4, (i*self.SQUARESIZE)-self.SQUARESIZE*0.4)
                    self.SCREEN.blit(self.SNKHEAD,loc)
                # Food
                elif self.board[i, j] == -1:
                    loc = (int((j+0.0)*self.SQUARESIZE), int((i+0.0)*self.SQUARESIZE))
                    self.SCREEN.blit(self.APPLE,loc)
        
        label = myfont2.render(f"Score: {self.score}", 1, self.BLACK)
        self.SCREEN.blit(label, (10,10))
        pygame.display.update() 

    def run_game(self, player_ai = None):
        update_rate = 3 # frames/update
        fps = 60
        counter = 0
        vel = self.vel
        myfont = pygame.font.SysFont("monospace", 65)
        self.draw_board()
        pygame.display.update()

        exit_flag = False
        while exit_flag == False and self.game_state == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_flag = True

                if event.type == pygame.KEYDOWN:
                    #Key Inputs
                    if event.key == pygame.K_UP:
                        vel = [-1, 0]
                    elif event.key == pygame.K_DOWN:
                        vel = [1, 0]
                    elif event.key == pygame.K_LEFT:
                        vel = [0, -1]
                    elif event.key == pygame.K_RIGHT:
                        vel = [0, 1]
                    else:
                        vel = self.vel
                    #Head Turning
                    if vel == [0,1]:
                        self.SNKHEAD = pygame.image.load("Img/Snake_Head.png")
                        self.SNKHEAD = pygame.transform.scale(self.SNKHEAD, (self.SQUARESIZE*1.8,self.SQUARESIZE*1.8))
                        self.SNKHEAD = pygame.transform.rotate(self.SNKHEAD, 90)
                    elif vel == [0,-1]:
                        self.SNKHEAD = pygame.image.load("Img/Snake_Head.png")
                        self.SNKHEAD = pygame.transform.scale(self.SNKHEAD, (self.SQUARESIZE*1.8,self.SQUARESIZE*1.8))
                        self.SNKHEAD = pygame.transform.rotate(self.SNKHEAD, -90)
                    elif vel == [1,0]:
                        self.SNKHEAD = pygame.image.load("Img/Snake_Head.png")
                        self.SNKHEAD = pygame.transform.scale(self.SNKHEAD, (self.SQUARESIZE*1.8,self.SQUARESIZE*1.8))
                    elif vel == [-1,0]:
                        self.SNKHEAD = pygame.image.load("Img/Snake_Head.png")
                        self.SNKHEAD = pygame.transform.scale(self.SNKHEAD, (self.SQUARESIZE*1.8,self.SQUARESIZE*1.8))
                        self.SNKHEAD = pygame.transform.rotate(self.SNKHEAD, 180)
            
            time.sleep(2.0/fps)
            counter += 1
            if counter >= update_rate:
                self.update_vel(vel)
                self.update_state()
                counter = 0
            self.draw_board()
            pygame.display.update()

        label = myfont.render(f"Game Over!", 1, self.RED)
        self.SCREEN.blit(label, (self.SQUARESIZE*5,self.SQUARESIZE*8))
        pygame.display.update()


        while exit_flag == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_flag = True
        pygame.quit()


def main():
    my_game = SnakeGameGUI()
    my_game.run_game()

if __name__ == "__main__":
    main()