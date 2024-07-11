import pygame, sys
from random import randint
pygame.init() 


WW = 600
WH = 600

cellsize = 20

screen = pygame.display.set_mode((WW, WH))
clock = pygame.time.Clock()





class Snake:
    def __init__(self):
        self.n = 3

        self.mas = [0] * self.n
        for i in range(self.n):
            self.mas[i] = pygame.Rect((WW / cellsize) // 2 * cellsize, (WH / cellsize) // 2 * cellsize + cellsize * i, cellsize, cellsize)

        self.direction = 'up'

        self.colorHead = (0, 0, 220)
        self.colorBody = (0, 0, 150)


    def move(self):
        for i in range(self.n-1, 0, -1):
            self.mas[i].x, self.mas[i].y = self.mas[i-1].x, self.mas[i-1].y

        if self.direction == 'left':
            self.mas[0].x -= cellsize

        if self.direction == 'right':
            self.mas[0].x += cellsize

        if self.direction == 'up':
            self.mas[0].y -= cellsize

        if self.direction == 'down':
            self.mas[0].y += cellsize


    def check_hit(self):
        if self.mas[0].x < 0 or self.mas[0].x > WW or self.mas[0].y < 0 or self.mas[0].y > WH:
            sys.exit()


    def eat(self):
        self.mas.append(pygame.Rect(self.mas[self.n-1].x, self.mas[self.n-1].y, cellsize, cellsize))
        self.n += 1



    def draw(self):
        pygame.draw.rect(screen, self.colorHead, self.mas[0])
        for i in range(1, self.n):
            pygame.draw.rect(screen, self.colorBody, self.mas[i])

        

class Apple:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, cellsize, cellsize)
        self.color = (200, 0, 0)


    def randpos(self):
        self.rect.x = randint(0, WW // cellsize) * cellsize
        self.rect.y = randint(0, WH // cellsize) * cellsize

    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)



player = Snake()
apple = Apple()
apple.randpos()




while True:
    screen.fill((50, 150, 50))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                player.direction = 'left'
            if e.key == pygame.K_d:
                player.direction = 'right'
            if e.key == pygame.K_w:
                player.direction = 'up'
            if e.key == pygame.K_s:
                player.direction = 'down'



    #pygame.draw.rect(screen, player.color, player)

    


    player.move()
    player.check_hit()

    if player.mas[0].colliderect(apple):
        apple.randpos()
        player.eat()


    player.draw()


    apple.draw()



    pygame.display.update()
    clock.tick(10)