import pygame
import time
import random


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
height = 600
width = 500
block_size = 10

class Snake:
   
    def __init__(self):
        self.x1 = 200
        self.y1 = 200
        self.x1_change = 0
        self.y1_change = 0
        self.body = []
        self.len = 1
        self.dir = None

    def draw(self,game):
        for x in self.body:
            pygame.draw.rect(game.dis, white, [x[0],x[1], block_size, block_size])
    # Changes direction based on key pressed
    def move(self,event):
        
        # Cannot move backwards
        if event.key == pygame.K_LEFT and self.dir != 'RIGHT':
            self.x1_change = -block_size
            self.y1_change = 0
            self.dir = 'LEFT'
        elif event.key == pygame.K_RIGHT and self.dir != 'LEFT':
            self.x1_change = block_size
            self.y1_change = 0
            self.dir = 'RIGHT'
        elif event.key == pygame.K_UP  and self.dir != 'DOWN':
            self.y1_change = -block_size
            self.x1_change = 0
            self.dir = 'UP'
        elif event.key == pygame.K_DOWN and self.dir != 'UP':
            self.y1_change = block_size
            self.x1_change = 0
            self.dir = 'DOWN'

    # Increases length of snake when it eats the yummies
    def eat(self,snack):
        # Check coordinates of snake and snack
        if self.x1 == snack.x and self.y1 == snack.y:
            self.len += 1
            print("Oishii!")
            return True
        return False

    # Resizes the snake as it moves to maintain its length
    def resize(self,x,y):
        self.body.append((x,y))
        if len(self.body) > self.len:
            del self.body[0]

    # Checks for collision with self or edges
    def check_collision(self, game):
        if self.x1 < 0 or self.x1 > height or self.y1 < 0 or self.y1 > width:
            game.running = False
        for x in self.body[:-1]:
            if x == (self.x1, self.y1):
                print(x)
                print(self.body)
                game.running = False

class Snack:
    def __init__(self):
        self.x = 50
        self.y = 50

    # Spanws a snack on screen 
    def spawn(self, game): 
        pygame.draw.rect(game.dis, red, [self.x, self.y, block_size, block_size])

class Game:
    def __init__(self):
        
        self.dis = pygame.display.set_mode((height, width))
        self.title = pygame.display.set_caption('Snake Game')
        self.running = True
        self.font = pygame.font.SysFont("comicsansms", 35)
        self.value = 0

    # Displays score on screen
    def score(self, snake):
        self.value = self.font.render("Score: " + str(snake.len -1), True, white)
        self.dis.blit(self.value, [0, 0])
 
 
def main():
    pygame.init()
    game = Game()
    snake = Snake()
    snack = Snack()
    
    clock = pygame.time.Clock()
    
    while game.running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            if event.type == pygame.KEYDOWN:
                snake.move(event)
        
        snake.x1 += snake.x1_change
        snake.y1 += snake.y1_change
        snake.check_collision(game)
        snake.resize(snake.x1,snake.y1)
        game.dis.fill(black)
        snake.draw(game)
        snack.spawn(game)
        game.score(snake)

        if snake.eat(snack):
            snack.x = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            snack.y = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            
        pygame.display.update()
        
        clock.tick(20)
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
